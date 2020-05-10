from database import Database 
import click 
from flask.cli import with_appcontext

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    database = Database()
    database.connect()
    database.create_tables()
    database.populate_combinatii()
