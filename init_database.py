#!/usr/bin/python3

import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "restaurants.db")

connection = sqlite3.connect(db_path)

print(connection.total_changes)

cursor = connection.cursor()
table_def = """CREATE TABLE restaurant (
                name TEXT, 
                address TEXT, 
                phone_number TEXT, 
                opening_time INTEGER, 
                closing_time INTEGER, 
                category TEXT, 
                takeout INTEGER, 
                delivery INTEGER, 
                menu TEXT)"""

cursor.execute(table_def)
connection.commit()


cursor.execute("INSERT INTO restaurant VALUES ('Momofoku', '123 Drury Ln', '867-5309', '09:00:00', '19:00:00', 'Japanese', '1', '1', 'ramen')")
cursor.execute("INSERT INTO restaurant VALUES ('Petit Crenn', '123 Polk St', '795-3000', '017:00:00', '23:00:00', 'French', '1', '1', 'ramen')")
connection.commit()

cursor.close()