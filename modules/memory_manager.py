from langdetect import detect

def detect_language(text):
    """Detects the language of the given text."""
    return detect(text)  # Returns 'te' for Telugu, 'hi' for Hindi, 'en' for English
