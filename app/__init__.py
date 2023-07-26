from flask import Flask
from app.config import Config
from app.extensions import db, migrate, loginmanager
from app.views import main_blueprint

BLUEPRINTS = [main_blueprint]
COMMANDS = []


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    # Flask-SLQAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate.init_app(app)


def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)
