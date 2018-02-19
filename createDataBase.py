# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 17:46:04 2018

@author: Clif
"""

import sqlite3 
from os.path import exists
from sys import exit

dbName = 'JobPostings.db'
if exists(dbName):
    exit()
    
conn = sqlite3.connect(dbName)
c = conn.cursor()
c.execute('''CREATE TABLE postings
              (postingID int PRIMARY KEY, 
              textID int, 
              title text, 
              authorID int)''')
c.execute('''CREATE TABLE authors
              (authorID int PRIMARY KEY, authorName text)''')
c.execute('''CREATE TABLE postingTexts
              (textID int PRIMARY KEY, postingText text)''')

conn.close()