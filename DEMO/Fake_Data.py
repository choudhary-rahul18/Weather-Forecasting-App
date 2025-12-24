import requests
from fastapi import FastAPI, HTTPException
import os
import httpx

server = FastAPI()

@server.get("/weather/{city}")
def fetch_weather(city:str):
    return {
      "location": {
        "name": "Agra",
        "region": "Uttar Pradesh",
        "country": "India",
        "lat": 27.1833,
        "lon": 78.0167,
        "tz_id": "Asia/Kolkata",
        "localtime_epoch": 1766550179,
        "localtime": "2025-12-24 09:52"
      },
      "current": {
        "last_updated_epoch": 1766549700,
        "last_updated": "2025-12-24 09:45",
        "temp_c": 17.0,
        "temp_f": 62.7,
        "is_day": 1,
        "condition": {
          "text": "Sunny",
          "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
          "code": 1000
        },
        "wind_mph": 8.5,
        "wind_kph": 13.7,
        "wind_degree": 295,
        "wind_dir": "WNW",
        "pressure_mb": 1018.0,
        "pressure_in": 30.05,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 37,
        "cloud": 0,
        "feelslike_c": 17.1,
        "feelslike_f": 62.7,
        "windchill_c": 17.1,
        "windchill_f": 62.7,
        "heatindex_c": 17.1,
        "heatindex_f": 62.7,
        "dewpoint_c": 2.2,
        "dewpoint_f": 36.0,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 1.6,
        "gust_mph": 11.2,
        "gust_kph": 18.0,
        "short_rad": 99.74,
        "diff_rad": 32.01,
        "dni": 0.0,
        "gti": 31.34
      }
    }

if __name__ == "__main__":
    import uvicorn, os
    uvicorn.run(
        "Fake_Data:server",
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 8050)),
    )
