"""This test the auth page"""

def test_request_of_welcome_page(client):
    """This makes the index page"""
    response = client.get("/auth/login")
    assert response.status_code == 200