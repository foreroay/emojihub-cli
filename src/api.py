import requests
from typing import List, Dict, Any

BASE_URL = "https://emojihub.yurace.pro/api"

def _make_request(endpoint: str) -> List[Dict[str, Any]] | Dict[str, Any] | None:
    """Helper function to make a GET request and handle errors."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: API request failed. {e}")
        return None

def get_random_emoji() -> Dict[str, Any] | None:
    """Fetches a single random emoji."""
    return _make_request("/random")

def get_all_groups() -> List[str] | None:
    """Fetches all emoji group names."""
    return _make_request("/groups")

def get_emojis_by_group(group_name: str) -> List[Dict[str, Any]] | None:
    """Fetches emojis from a specific group."""
    return _make_request(f"/all/group/{group_name}")

def search_emojis(query: str) -> List[Dict[str, Any]] | None:
    """Searches for emojis by name."""
    return _make_request(f"/search?q={query}")
