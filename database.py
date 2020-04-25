#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Beatrice Caruntu
#-----------------------------------------------------------------------

from sqlite3 import connect
from sys import stderr
from os import path
import numpy as np
import pandas as pd

#-----------------------------------------------------------------------
class Database:
    
    def __init__(self):
        self._connection = None

    def connect(self):      
        DATABASE_NAME = 'DATABASE_URL'
        self._connection = connect(DATABASE_NAME)
                    
    def disconnect(self):
        self._connection.close()
#-----------------------------------------------------------------------
    def create_tables(self):
        cursor = self._connection.cursor()
        combinatii = 'CREATE TABLE [IF NOT EXISTS] combinatii (q_id INTEGER, a_id INTEGER, score FLOAT);'
        cursor.execute(combinatii)
        self._connection.commit()
        cursor.close()
        return
#-----------------------------------------------------------------------    
    # Populate the initial combinatii table with q_id and a_id pairs
    def populate_combinatii(self):
        cursor = self._connection.cursor()
     
        comanda = 'INSERT INTO combinatii (q_id, a_id) VALUES (?, ?);'   
        for i in range(0, 117):
            for j in range(0, 206):
                cursor.execute(comanda, [i, j,])
                self._connection.commit()
        cursor.close()    
        return
#-----------------------------------------------------------------------    
    # Adauga combinatii 
    def combinatii(self, qid, winner, loser1, loser2, loser3):
        arguments = []
        cursor = self._connection.cursor()
        comanda_win = 'UPDATE combinatii  SET score = score+1 WHERE q_id = ? AND a_id = ?;'
        comanda_lose = 'UPDATE combinatii  SET score = score-0.25 WHERE q_id = ? AND a_id = ?;'
        cursor.execute(comanda_win, [qid, winner,])
        self._connection.commit()
        cursor.execute(comanda_lose, [qid, loser1,])
        self._connection.commit()
        cursor.execute(comanda_lose, [qid, loser2,])
        self._connection.commit()
        cursor.execute(comanda_lose, [qid, loser3,])
        self._connection.commit()
        cursor.close()
        return   
#-----------------------------------------------------------------------

# For testing:

if __name__ == '__main__':
    database = Database()
    database.connect()
    courses = database.search('', '','','')
    for course in courses:
        print(course)
    database.disconnect()
