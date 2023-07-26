import click
from app.extensions import db
from flask.cli import with_appcontext


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Database Created")


@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Creating Test Data")

    click.echo("Test Data Created")
