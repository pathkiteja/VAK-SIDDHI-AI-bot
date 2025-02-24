import webbrowser
import json

URL_FILE = "data/urls.json"

def save_url(name, url):
    """Saves a website shortcut."""
    with open(URL_FILE, "r+") as file:
        data = json.load(file)
        data[name] = url
        file.seek(0)
        json.dump(data, file)

def open_url(name):
    """Opens a saved website shortcut."""
    with open(URL_FILE, "r") as file:
        data = json.load(file)
        if name in data:
            webbrowser.open(data[name])
