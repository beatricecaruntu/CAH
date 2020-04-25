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
class Card:
    
    def __init__(self):
        self._connection = None

    def connect(self):      
        DATABASE_NAME = 'cards.db'
        self._connection = connect(DATABASE_NAME)
                    
    def disconnect(self):
        self._connection.close()

    
#-----------------------------------------------------------------------    
    def random_q(self):
        cursor = self._connection.cursor()
        comanda = 'SELECT q_id, question FROM cards ORDER BY RANDOM() LIMIT 1;'
        cursor.execute(comanda)
        question = cursor.fetchone()
        return question 
#-----------------------------------------------------------------------    
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
