#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Beatrice Caruntu
#-----------------------------------------------------------------------

from sqlite3 import connect
from sys import stderr
from os import path

#-----------------------------------------------------------------------

class Database:
    
    def __init__(self):
        self._connection = None

    def connect(self):      
        DATABASE_NAME = 'DATABASE_URL'
        if not path.isfile(DATABASE_NAME):
            raise Exception('Database connection failed')
        self._connection = connect(DATABASE_NAME)
                    
    def disconnect(self):
        self._connection.close()

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
    
    def random_q(self):
        cursor = self._connection.cursor()
        comanda = 'SELECT q_id, question FROM cards ORDER BY RANDOM() LIMIT 1;'
        cursor.execute(comanda)
        question = cursor.fetchone()
        return question 
    
    def random_a(self):
        cursor = self._connection.cursor()
        comanda = 'SELECT a_id, answer FROM answers ORDER BY RANDOM() LIMIT 1;'
        cursor.execute(comanda)
        question = cursor.fetchone()
        return question 
        

#-----------------------------------------------------------------------

# For testing:

if __name__ == '__main__':
    database = Database()
    database.connect()
    courses = database.search('', '','','')
    for course in courses:
        print(course)
    database.disconnect()
