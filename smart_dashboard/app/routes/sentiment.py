from fastapi import APIRouter, Query
from ..ml.sentiment_model import analyze_sentiment

router = APIRouter(prefix="/sentiment", tags=["Sentiment Analysis"])

@router.get("/")
def get_sentiment(text: str = Query(..., description="Enter text to analyze sentiment")):
    """
    Analyze the sentiment of a given text using TextBlob.
    Example:
    /sentiment?text=I love this dashboard!
    """
    return analyze_sentiment(text)
