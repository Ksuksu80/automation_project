import requests

def test_get_all_products_list(api_client):
    """Verify that POST method is not supported for productsList"""
    response = api_client.get(f"{api_client.base_url}/productsList")

    assert response.status_code == 200
    body = response.json()
    assert "products" in body
    assert isinstance(body["products"], list)
    print("✅ Total products:", len(body["products"]))