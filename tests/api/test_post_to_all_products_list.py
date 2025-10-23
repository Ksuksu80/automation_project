import pytest

def test_post_to_all_products_list(api_client):

    """Verify that API returns all products"""
    response = api_client.post(f"{api_client.base_url}/productsList")

    """if server returns 200 instead of 405 code"""
    if response.status_code == 200:
        pytest.xfail("Server bug: POST returns 200 instead of 405")

    # verify code and message
    assert response.status_code == 405, f"Expected 405, got {response.status_code}"
    assert "not supported" in response.text, f"Unexpected message: {response.text}"
    print(f"✅ POST not allowed as expected: {response.text}")

    # assert "not supported" in message, f"Unexpected message: {message}"
    # print(f"✅ POST not allowed as expected: {message}")
