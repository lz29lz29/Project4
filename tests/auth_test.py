"""This test the auth page"""

def test_request_of_login_page(client):
    """This makes the index page"""
    response = client.get("/login")
    assert response.status_code == 200


def test_login_example(client):
    """This makes the index page"""
    response = client.get("/login")
    assert b"login" in response.data


def test_register_example(client):
    """This makes the index page"""
    response = client.get("/register")
    assert response.status_code == 200


def test_logout_example(client):
    """This makes the index page"""
    response = client.get("/logout")
    assert response.status_code == 302


def test_dashboard_example(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302