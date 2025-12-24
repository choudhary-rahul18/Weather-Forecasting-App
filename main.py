from dotenv import load_dotenv
import os, httpx, time
from fastapi import FastAPI, HTTPException, Request
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()                  # Still shows them in your terminal
    ]
)
logger = logging.getLogger("WeatherAPI")

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

origins_str = os.getenv("ALLOWED_ORIGINS", "")
origins_list = origins_str.split(",") if origins_str else []


# We use 'get_remote_address' to track users by their IP
limiter = Limiter(key_func=get_remote_address)

# 1. LIFESPAN: This manages the 'AsyncClient' for the whole app
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup: Create the client when app starts
    app.state.http_client = httpx.AsyncClient(timeout=30.0)
    yield
    # Cleanup: Close the client when app stops
    await app.state.http_client.aclose()

app = FastAPI(title="Weather API", version="1.0.0", lifespan=lifespan)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins_list, # Now this is a dynamic list!
    allow_credentials=True,     # Necessary if you use cookies or tokens
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/weather/{city}")
#APPLY THE LIMIT: 15 requests per minute per IP
@limiter.limit("15/minute")
async def fetch_weather(request: Request, city: str):
    
    try:
        if not api_key:
            raise HTTPException(status_code=500, detail="API key not configured")
        url = "http://api.weatherapi.com/v1/current.json"
        params = {"key": api_key, "q": city}
        response = await app.state.http_client.get(url, params=params)
        

        # Check for specific authentication/permission errors
        if response.status_code != 200:
            logger.error(f"Upstream API Failure | City: {city} ")
        if response.status_code == 401:
            raise HTTPException(status_code=503, detail="Weather station authentication failed. We're on it!")
        if response.status_code == 403:
            raise HTTPException(status_code=503, detail="Our API access is temporarily restricted. Please try later.")
            

        response.raise_for_status()
        data = response.json()
        # 2. Second, safely extract with validation or defaults
        if "location" not in data or "current" not in data:
            raise HTTPException(
                status_code=502, 
                detail="External API returned an incomplete response structure"
            )

        return {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "time": data["location"]["localtime"],
            "temp": data["current"]["temp_c"],
            "icon": f"https:{data['current']['condition']['icon']}",
            "condition": data["current"]["condition"]["text"],
            "wind_kph": data["current"]["wind_kph"],
            "humidity": data["current"]["humidity"]
        }

    except httpx.HTTPStatusError as exc:
    # Handle the "Nap" scenario for general server issues
        logger.critical(f"System Crash: {str(exc)}")
        raise HTTPException(status_code=500, detail="The weather station is taking a nap. Try again soon!")
    

