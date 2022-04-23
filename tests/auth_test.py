"""This test the auth page"""

def test_request_of_login_page(client):
    """This makes the index page"""
    response = client.get("/auth/login")
    assert response.status_code == 200


def test_login_example(client):
    """This makes the index page"""
    response = client.get("/auth/login")
    assert b"login" in response.data


def test_register_example(client):
    """This makes the index page"""
    response = client.get("/auth/register")
    assert response.status_code == 200