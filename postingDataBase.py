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
                  (postingID int PRIMARY KEY, 
                  postingText text, 
                  title text, 
                  author text)''')
    
    conn.close()
    
def insert_into_db():
    pass
