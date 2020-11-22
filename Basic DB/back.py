import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , date text , study integer , reading text , programming text , walking text ,movie text)")
    conn.commit()
    conn.close()

def insert(date , study , reading , programming , walking , movie):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (date , study , reading , programming , walking , movie))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , study='' , reading='' , programming='' , walking='' , movie=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=?  OR study=? OR reading=? OR programming=? OR walking=? OR movie=?" , (date , study , reading , programming , walking , movie))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
