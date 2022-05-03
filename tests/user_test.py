import logging
import os

from app import db
from app.db.models import User, Transaction
from faker import Faker


def test_user_song_table(application):

    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0

