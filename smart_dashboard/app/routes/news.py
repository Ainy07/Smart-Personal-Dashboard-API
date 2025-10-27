from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

NEWS_API_KEY = os.getenv("NEWS_API_KEY", "cce748449e234c9c9806bb531cdadf8c")  

@router.get("/")
def get_top_headlines(country: str = "us"):
    """
    Fetch top news headlines from NewsAPI.org
    """
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data
