import sqlite3
import csv 


def create_database():
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    table_q1 = '''CREATE TABLE IF NOT EXISTS unigrams(
        id INTEGER PRIMARY KEY,
        w1 TEXT NOT NULL,
        score REAL NOT NULL
    );'''
    table_q2 = '''CREATE TABLE IF NOT EXISTS bigrams(
        id INTEGER PRIMARY KEY,
        w1 TEXT NOT NULL,
        w2 TEXT NOT NULL,
        score REAL NOT NULL
    );'''
    table_q3 = '''CREATE TABLE IF NOT EXISTS trigrams(
        id INTEGER PRIMARY KEY,
        w1 TEXT NOT NULL,
        w2 TEXT NOT NULL,
        w3 TEXT NOT NULL,
        score REAL NOT NULL
    );'''
    try:
        cur.execute(table_q1)
        cur.execute(table_q2)
        cur.execute(table_q3)
    except Exception as e:
        print(e)
    finally:
        con.commit()
        con.close()


def populate_db_table(path_csv, db_name, table_name):
    con = open(path_csv, encoding="utf-8")
    reader = csv.DictReader(con, delimiter=",")
    headers = reader.fieldnames
    db = sqlite3.connect(db_name)
    cur = db.cursor()
    for idx, row in enumerate(reader):
        vals = [idx]+[row[k] for k in headers]
        vals = tuple(vals)
        q = f'''
        INSERT INTO {table_name} VALUES {vals}
        '''
        cur.execute(q)
    db.commit()
    db.close()
