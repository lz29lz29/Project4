"""This test the simple page"""

def test_request_of_welcome_page(client):
    """This makes the index page"""
    response = client.get("/welcome")
    assert response.status_code == 200


def test_request_example(client):
    """This makes the index page"""
    response = client.get("/welcome")
    assert b"Welcome" in response.data


def test_request_of_about_page(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200

def test_about_page_data(client):
    """This makes the index page"""
    response = client.get("/about")
    assert b"About" in response.data