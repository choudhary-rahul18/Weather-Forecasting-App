from dotenv import load_dotenv
import requests
import os, httpx
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")
FAKE_API_URL = os.getenv("FAKE_API_URL")
USE_FAKE_API = True

app = FastAPI(title="Weather API", version="1.0.0")


@app.get("/weather/{city}")
async def fetch_weather(city: str):
    if not api_key:
        raise HTTPException(status_code=500, detail="API key not configured")

    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}

    
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            if USE_FAKE_API:
                response = await client.get(
                    f"{FAKE_API_URL}/{city}"
                )
            else:
                if not api_key:
                    raise HTTPException(status_code=500, detail="API key not configured")
                url = "http://api.weatherapi.com/v1/current.json"
                params = {"key": api_key, "q": city}
                response = await client.get(url, params=params)

            response.raise_for_status()

            # Specific error handling based on status codes
            if response.status_code == 401:
                raise HTTPException(status_code=401, detail="Invalid API Key")
            elif response.status_code == 400:
                raise HTTPException(status_code=404, detail="City not found or invalid input")
            
            
            data = response.json()

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

    except httpx.ConnectError:
        raise HTTPException(status_code=503, detail="Weather service is down")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


# import json
# DATA_FILE = "weather_raw_data.json"
# def save_raw_weather_response(raw_data):
#     record = {
#         "data": raw_data
#     }

#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as f:
#             try:
#                 existing = json.load(f)
#             except json.JSONDecodeError:
#                 existing = []
#     else:
#         existing = []

#     existing.append(record)

#     with open(DATA_FILE, "w") as f:
#         json.dump(existing, f, indent=2)