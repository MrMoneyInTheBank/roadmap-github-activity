import requests
from typing import Any, List


def get_activity(username: str) -> List[Any]:
    url = f"https://api.github.com/users/{username}/events"
    response = None
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses

    except requests.exceptions.HTTPError as http_err:
        if not response:
            return []
        if response.status_code == 404:
            print(f"User '{username}' not found.")
        elif response.status_code == 403:
            print("Rate limit exceeded. Try again later.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return []

    except requests.exceptions.RequestException as err:
        print(f"Error connecting to GitHub API: {err}")
        return []

    # If everything went well, parse and return only the 5 most recent events
    events = response.json()
    return events[:5]
