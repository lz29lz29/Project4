import logging
import os

from app import db
from app.db.models import User, Transaction
from faker import Faker
from pathlib import Path

def test_register(client):
    """This makes the index page"""
    data = {
        'email': 'aaa111@test.com',
        'password': 'zzz123',
        'confirm': 'zzz123'
    }
    client.post("/register", data = data)
    user = User.query.filter_by(email='aaa111@test.com').first()
    assert user.email == 'aaa111@test.com'



def test_login(client):
    """This makes the index page"""
    data = {
        'email': 'aaa111@test.com',
        'password': 'zzz123',
        'confirm': 'zzz123'
    }
    client.post("/register", data = data)
    user = User.query.filter_by(email='aaa111@test.com').first()
    assert user.email == 'aaa111@test.com'
    data1 = {
        'email': 'aaa111@test.com',
        'password': 'zzz123',
    }

    client.post("/login", data = data1)
    user = User.query.filter_by(email='aaa111@test.com').first()
    assert user.authenticated == True