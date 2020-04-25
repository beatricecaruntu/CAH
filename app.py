#!/usr/bin/env python

#-----------------------------------------------------------------------
# web.py
# Author: Beatrice Caruntu
#-----------------------------------------------------------------------

from sys import argv
from database import Database
from cards import Card
from flask import Flask, request, make_response, redirect, url_for, session
from flask import render_template
import os
import re
import click 
from flask.cli import with_appcontext
#-----------------------------------------------------------------------

app = Flask(__name__, template_folder='.')
app.secret_key = "super secret key"

#-----------------------------------------------------------------------
@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
    database = Database()
    database.connect()
    card = Card()
    card.connect()
    if not session.get('q'): 
        session['q'] = card.random_q()                  
    if not session.get('1'):
        session['1'] = card.random_a()
    if not session.get('2'):
        session['2'] = card.random_a()
    if not session.get('3'):
        session['3'] = card.random_a()
    if not session.get('4'):
        session['4'] = card.random_a()
        
    q = session['q'][0]
    if request.method == 'POST':         
        session['q'] = card.random_q()   
        if request.form['submit']=='1': 
            database.combinatii(qid=q, winner=session['1'][0], loser1=session['2'][0], loser2=session['3'][0], loser3=session['4'][0])
            session['1'] = card.random_a()
            
        elif request.form['submit']=='2':
            database.combinatii(qid=q, winner=session['2'][0], loser1=session['1'][0], loser2=session['3'][0], loser3=session['4'][0])
            session['2'] = card.random_a()
            
        elif request.form['submit'] == '3':
            database.combinatii(qid=q, winner=session['3'][0], loser1=session['2'][0], loser2=session['1'][0], loser3=session['4'][0])
            session['3'] = card.random_a()
            
        elif request.form['submit'] == '4':
            database.combinatii(qid=q, winner=session['4'][0], loser1=session['2'][0], loser2=session['3'][0], loser3=session['1'][0])
            session['4'] = card.random_a()
            
    return render_template('cards.html', question=session['q'][1], answer1=session['1'][1], answer2=session['2'][1], answer3=session['3'][1], answer4=session['4'][1])

@app.route("/refresh")
def refresh():
    session.pop('1', None)
    session.pop('2', None)
    session.pop('3', None)
    session.pop('4', None)
    # Redirect to main page
    return redirect(url_for('index'))

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    Database.create_all()
#-----------------------------------------------------------------------

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
        
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    #sess.init_app(app)

    app.debug = True  
    app.run(host='localhost', port=int(argv[1]), debug=True)