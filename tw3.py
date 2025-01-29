main.py

import sqlite3

def init_db():
   conn = sqlite3.connect(':memory:')
   cursor = conn.cursor()
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   name TEXT,
   age INTEGER)
   ''')
   return conn

def add_user(conn, name, age):
   cursor = conn.cursor()
   cursor.execute('''
   INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
   conn.commit()

def get_user(conn, name):
   cursor = conn.cursor()
   cursor.execute('''SELECT * FROM users WHERE name=?''', (name,))
   return cursor.fetchone()


test.py

import pytest
from main import init_db, add_user, get_user


@pytest.fixture
def db_conn():
   conn = init_db()
   yield conn
   conn.close()

def test_add_or_get_user(db_conn):
   add_user(db_conn, "Sasha", 30)
   user = get_user(db_conn, "Sasha")
   assert user == (1, "Sasha", 30)

