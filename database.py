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
import psycopg2

#-----------------------------------------------------------------------
heroku = False

class Database:
    
    def __init__(self):
        self._connection = None

    def connect(self):  
        if heroku:    
            DATABASE_URL = 'postgres://rimxapgmsmovie:0f7e87fc6f146b8af081eb59db366866a99f2dfbbf8e8d5b0fed91b168ef0de7@ec2-34-233-186-251.compute-1.amazonaws.com:5432/dcrl8c4kcd58ol'
            self._connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        else:
            conn_string = "host='localhost' dbname='cah' user='postgres'"
            self._connection = psycopg2.connect(conn_string)   

        # if not path.isfile(DATABASE_NAME):
        #     raise Exception("database reeats.db not found")
        # self._connection = connect(DATABASE_NAME)
        # self._connection = psycopg2.connect(DATABASE_URL, sslmode='require')
        # self._connection = psycopg2.connect(conn_string)   

                    
    def disconnect(self):
        self._connection.close()
#-----------------------------------------------------------------------
    def create_tables(self):
        cursor = self._connection.cursor()
        combinatii = 'CREATE TABLE IF NOT EXISTS combinatii (q_id INTEGER, a_id INTEGER, score FLOAT);'
        cursor.execute(combinatii)
        self._connection.commit()
        cursor.close()
        return
#-----------------------------------------------------------------------   
    def initial_insert(self):
        print("initial_insert")
        cursor = self._connection.cursor()
        
        qts = pd.read_excel('questions.xlsx')
        qts_np = np.array(qts)
        comanda = 'INSERT INTO cards (id, question) VALUES (%s, %s);'        
        for i in range(0, qts_np.size):
            cursor.execute(comanda, [i, str((qts_np[i,0])),])
            self._connection.commit()
            
        ans = pd.read_excel('answrs.xlsx')
        ans_np = np.array(ans)
        comanda = 'INSERT INTO answers (ans_id, answer) VALUES (%s, %s);'        
        for i in range(0, ans_np.size):
            cursor.execute(comanda, [i, str((ans_np[i,0])),])
            self._connection.commit()
        cursor.close()        
        return
    
    
#-----------------------------------------------------------------------    
    # Populate the initial combinatii table with q_id and a_id pairs
    def populate_scores(self):
        print("populate_scores")
        cursor = self._connection.cursor()
     
        comanda = 'INSERT INTO scores (id, ans_id, score) VALUES (%s, %s, %s);'   
        for i in range(0, 117):
            for j in range(0, 206):
                cursor.execute(comanda, [i, j, 0])
                self._connection.commit()
        cursor.close()    
        return
#-----------------------------------------------------------------------    
    # Adauga combinatii  SET order_id = %s
    def combinatii(self, qid, winner, loser1, loser2, loser3):
        arguments = []
        cursor = self._connection.cursor()
        comanda_win = 'UPDATE scores SET score = score+3 WHERE id = %s AND ans_id = %s;'
        comanda_lose = 'UPDATE scores SET score = score-1 WHERE id = %s AND ans_id = %s;'
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
    database.initial_insert()
    database.populate_scores()
    database.disconnect()
