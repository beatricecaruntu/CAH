from database import Database 

database = Database()
database.connect()
database.create_tables()
database.populate_combinatii()
