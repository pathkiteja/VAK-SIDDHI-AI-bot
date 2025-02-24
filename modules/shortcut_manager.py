import json

SHORTCUTS_FILE = "data/shortcuts.json"

def save_shortcut(name, action):
    """Saves a shortcut action."""
    with open(SHORTCUTS_FILE, "r+") as file:
        data = json.load(file)
        data[name] = action
        file.seek(0)
        json.dump(data, file)

def execute_shortcut(name):
    """Executes a saved shortcut."""
    with open(SHORTCUTS_FILE, "r") as file:
        data = json.load(file)
        return data.get(name, "Shortcut not found.")
