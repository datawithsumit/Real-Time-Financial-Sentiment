import random
import datetime
from textblob import TextBlob

tickers = ["AAPL", "TSLA", "GOOGL", "AMZN", "MSFT"]

headlines = [
    "Stock hits all-time high after earnings report",
    "CEO steps down, investors are worried",
    "New product launch creates massive hype",
    "Supply chain issues cause major delays",
    "Quarterly revenue exceeds expectations",
    "Lawsuit filed against the company for privacy violations",
    "Market crashes as inflation fears rise",
    "Company announces huge buyback program"
]

def get_live_data():
    """
    Generates a single data point: A stock, a timestamp, a headline,
    and the AI-calculated sentiment score.
    """
    ticker = random.choice(tickers)
    headline = random.choice(headlines)
    now = datetime.datetime.now().strftime("%H:%M:%S")

    blob = TextBlob(headline)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        mood = "Positive"
    elif sentiment_score < 0:
        mood = "Negative"
    else:
        mood = "Neutral"

    return {
        "time": now,
        "ticker": ticker,
        "headline": headline,
        "score": sentiment_score,
        "mood": mood
    }

if __name__ == "__main__":
    print(get_live_data())
