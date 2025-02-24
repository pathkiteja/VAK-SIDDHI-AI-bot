import random

responses = {
    "How are you?": ["I'm doing great!", "Feeling awesome today!", "I'm good, thanks! How about you?"],
}

def get_response(user_input):
    """Returns a varied response for repeated questions."""
    return random.choice(responses.get(user_input, ["I don't understand."]))
