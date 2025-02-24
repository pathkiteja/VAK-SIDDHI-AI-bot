from modules.speech_handler import recognize_speech, text_to_speech
from modules.sentiment_analysis import detect_mood
from modules.memory_manager import save_preference, get_preference, reset_memory
from modules.language_detection import detect_language
from modules.url_manager import save_url, open_url
from modules.chatbot_responses import get_response

def chatbot():
    """Main chatbot loop."""
    while True:
        user_input = input("You: ")
        mood = detect_mood(user_input)
        response = f"Looks like you're feeling {mood}. How can I help?"
        text_to_speech(response)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
