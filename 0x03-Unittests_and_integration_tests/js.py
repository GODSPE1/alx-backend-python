import requests

def get_json(url: str) -> dict:
    """fetch JSON data from a URL and retur t as a dictionary."""
    response = requests.get(url)
    requests.raise_for_status()
    return response.json()