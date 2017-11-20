import sqlite3

conn = sqlite3.connect('data.db')

c = conn.cursor()

c.execute(""" CREATE TABLE data(
            Name text,
            body text,
            time blob
            )""")


conn.commit()

conn.close()