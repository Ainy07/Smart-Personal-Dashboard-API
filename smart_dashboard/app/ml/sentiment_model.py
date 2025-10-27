from textblob import TextBlob

def analyze_sentiment(text: str):
    """
    Analyze sentiment of a given text using TextBlob.
    Returns sentiment label (Positive / Negative / Neutral) and polarity score.
    """
    if not text or not text.strip():
        return {"error": "Text cannot be empty"}

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  

    if polarity > 0.1:
        sentiment = "Positive 😊"
    elif polarity < -0.1:
        sentiment = "Negative 😔"
    else:
        sentiment = "Neutral 😐"

    return {
        "text": text,
        "polarity": round(polarity, 3),
        "sentiment": sentiment
    }
