import click 
from database import Database as database
from flask.cli import with_appcontext

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    database.create_all()