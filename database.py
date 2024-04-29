from flask import Flask
import sqlite3

#DB class
class dbAPI:

    def __init__(self, db_name):
        self.db_name = db_name   
    
    def get_db_connection(self):
        connection = sqlite3.connect('tasktodo.db')
        connection.row_factory = sqlite3.Row
        return connection

    def get_db_cursor(self, connection):
        cursor = connection.cursor()
        return cursor

    def create_db_table(self):
        connection = self.get_db_connection()
        cursor = self.get_db_cursor(connection)
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks_new (
                   id INTEGER PRIMARY KEY,
                   task TEXT
        )''')
        connection.commit()
        connection.close()
