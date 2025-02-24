import numpy as np
import json
import random

# Define state-action Q-table
Q_table = {}

# Load existing model if available
try:
    with open("models/chatbot_rl_model.pkl", "r") as f:
        Q_table = json.load(f)
except FileNotFoundError:
    Q_table = {}

# Define rewards for chatbot responses
rewards = {
    "positive": 10,
    "neutral": 5,
    "negative": -10
}

def update_q_table(state, action, reward, next_state):
    """Updates the Q-table using Q-learning formula."""
    learning_rate = 0.1
    discount_factor = 0.9

    if state not in Q_table:
        Q_table[state] = {}

    if action not in Q_table[state]:
        Q_table[state][action] = 0

    Q_table[state][action] = Q_table[state][action] + learning_rate * (reward + discount_factor * max(Q_table.get(next_state, {}).values(), default=0) - Q_table[state][action])

    # Save updated model
    with open("models/chatbot_rl_model.pkl", "w") as f:
        json.dump(Q_table, f)

def choose_action(state):
    """Chooses the best action based on Q-table."""
    if state in Q_table and random.random() > 0.2:  # 80% chance to exploit
        return max(Q_table[state], key=Q_table[state].get, default="neutral_response")
    else:
        return random.choice(["positive_response", "neutral_response", "negative_response"])  # 20% chance to explore

def get_rl_response(user_input, sentiment):
    """Generates chatbot response using RL model."""
    state = user_input.lower()
    action = choose_action(state)

    if action == "positive_response":
        response = "That sounds great! Keep up the good vibes!"
        reward = rewards["positive"]
    elif action == "negative_response":
        response = "I'm sorry you're feeling this way. Try taking a deep breath."
        reward = rewards["negative"]
    else:
        response = "I see. Let's talk more about it."
        reward = rewards["neutral"]

    update_q_table(state, action, reward, next_state="conversation_continues")
    return response
