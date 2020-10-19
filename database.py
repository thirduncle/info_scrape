import sqlite3

connection = sqlite3.connect('infowar.db')

def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS shows (date TEXT, title TEXT, url TEXT);"
        )

def add_entry(date, title, url):
    with connection:
        connection.execute(
            "INSERT INTO shows VALUES (?, ?, ?);", (date, title, url)
        )