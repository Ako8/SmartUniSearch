from flask import Blueprint, render_template
from os import path
from app.config import Config


TEMPLATE_FOLDER = path.join(Config.BASE_DIRECTORY, 'templates', 'main')
main_blueprint = Blueprint('main', __name__, template_folder=TEMPLATE_FOLDER)


@main_blueprint.route("/")
def home():
    return render_template("home.html")
