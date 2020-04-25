from database import Database 

database = Database()
database.connect()
database.create_all()
database.populate_cards()
database.populate_answers()
database.populate_combinatii()
