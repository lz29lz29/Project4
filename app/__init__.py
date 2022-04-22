"""A simple flask web app"""
import os
from flask import Flask, render_template, Blueprint
from app.cli import create_database
from app.db import db
from app.db.models import User
from flask_bootstrap import Bootstrap5
from app.simple_pages import simple_pages
from app.auth import auth
from app.context_processors import utility_text_processors


def page_not_found(e):
    return render_template("404.html"), 404

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'

    app.register_error_handler(404, page_not_found)

    db_dir = "database/db.sqlite"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    bootstrap = Bootstrap5(app)
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.context_processor(utility_text_processors)
    # add command function to cli commands
    app.cli.add_command(create_database)



    return app