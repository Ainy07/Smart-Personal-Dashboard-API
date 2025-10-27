from fastapi import APIRouter, HTTPException
import requests

router = APIRouter() 

@router.get("/")
def get_weather(city: str):
    api_key = "68000283f24b597c6ec0a31463606fe8"  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="City not found or API error")

    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
