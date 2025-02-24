from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def detect_mood(user_input):
    """Detects sentiment using BERT model."""
    result = sentiment_pipeline(user_input)
    sentiment_label = result[0]['label']
    
    if sentiment_label == "POSITIVE":
        return "happy"
    elif sentiment_label == "NEGATIVE":
        return "sad"
    else:
        return "neutral"
