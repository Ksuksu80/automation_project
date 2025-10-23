import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    """basic url API."""
    return "https://automationexercise.com/api"


@pytest.fixture(scope="session")
def api_client(base_url):
    """HTTP client with common headers and session"""
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "User-Agent": "AutomationProject/1.0"
    })
    session.base_url = base_url  # just for convenience
    yield session
    session.close()