import pytest
from unittest.mock import patch, MagicMock
from src.api import get_random_emoji

@patch("src.api.requests.get")
def test_api_error_returns_none(mock_get):
    """Simulate an HTTP error to ensure graceful failure handling."""
    mock_response = MagicMock()
    # Simulate a failed response when .raise_for_status() is called
    mock_response.raise_for_status.side_effect = Exception("API failed")
    mock_get.return_value = mock_response

    result = get_random_emoji()

    # The function should catch the error and return None
    assert result is None
