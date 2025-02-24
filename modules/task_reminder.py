import time

def set_reminder(message, delay):
    """Sets a reminder after a given time delay."""
    time.sleep(delay)
    print(f"Reminder: {message}")
