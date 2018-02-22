# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:46:04 2018

@author: Clif
"""

import sqlite3 
from os.path import exists

def create_db():
    dbName = 'JobPostings.db'
    if exists(dbName):
        return    
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    c.execute('''CREATE TABLE postings
                  (postingID INTEGER PRIMARY KEY AUTOINCREMENT, 
                  postingText text, 
                  title text, 
                  author text)''')
    conn.commit()  
    conn.close()
    
def insert_into_db(text, title, author):
    conn = sqlite3.connect("JobPostings.db")
    c = conn.cursor()
    tup = (text, title, author)
    c.execute('''INSERT INTO 
              postings(postingText, title, author) 
              VALUES(?,?,?)''', tup)
    conn.commit()
    conn.close()

