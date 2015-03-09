from flask import Flask, render_template

from . import models
from .extensions import db, migrate, config
from .views import github


SQLALCHEMY_DATABASE_URI = "postgres://localhost/github"
DEBUG = True
SECRET_KEY = 'development-key'
DEBUG_TB_INTERCEPT_REDIRECTS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.register_blueprint(github)

    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app