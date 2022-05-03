import logging
import os

from app import db
from app.db.models import User, Transaction
from faker import Faker


def test_user_song_table(application):

    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0


def test_adding_user(application):

    with application.app_context():
        user = User('aaa111@google.com', 'zxc123')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1


def test_query_user(application):

    with application.app_context():
        user = User('aaa111@google.com', 'zxc123')
        db.session.add(user)
        db.session.commit()
        user1 = User.query.filter_by(email='aaa111@google.com').first()
        assert user1.email == 'aaa111@google.com'


def test_add_transaction(application):

    with application.app_context():
        user = User('aaa111@google.com', 'zxc123')
        db.session.add(user)
        db.session.commit()
        user1 = User.query.filter_by(email='aaa111@google.com').first()
        user1.transactions = [Transaction("200","CREDIT")]
        db.session.commit()
        assert db.session.query(Transaction).count() == 1


def test_delete_user(application):

    with application.app_context():
        user = User('aaa111@google.com', 'zxc123')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        db.session.delete(user)
        assert db.session.query(User).count() == 0


def test_add_transactions(application):

    with application.app_context():
        user = User('aaa111@google.com', 'zxc123')
        db.session.add(user)
        db.session.commit()
        user1 = User.query.filter_by(email='aaa111@google.com').first()
        user1.transactions = [Transaction("200","CREDIT"), Transaction("100","CREDIT")]
        db.session.commit()
        assert db.session.query(Transaction).count() == 2

