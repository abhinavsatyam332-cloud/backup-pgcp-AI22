import os
import sqlite3
from sqlite3 import Error


def getConnection(d_path):
    try:
        conn = sqlite3.connect(d_path)
        print("Conn success")
        return conn
    except Error as er:
        print(f"Connection Failed: {er}")
        return None


def exec_query(conn, query):
    # Guard clause to prevent NoneType errors if connection failed
    if conn is None:
        print("Skipping query execution: No active database connection.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as er:
        print(f"Execution Error: {er}")


def exec_read_query(conn, query):
    if conn is None:
        print("Skipping read query: No active database connection.")
        return None

    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        print("Read query executed successfully")
        return result
    except Error as er:
        print(f"Read Error: {er}")
        return None

def show(con):
    users = exec_read_query(con, fetch_users)
    if users:
        print("\n--- User Records ---")
        for u in users:
            print(u)

# --- SQL Queries ---

# FIX: Changed 'AUTO_INCREMENT' to 'INTEGER PRIMARY KEY AUTOINCREMENT'
create_table = """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);"""

add_users = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""

fetch_users = """SELECT * from users;"""


update_user = """
UPDATE 
    users
SET
    age = 22
WHERE 
    name = 'Mike'
"""

delete_user = """
DELETE from users WHERE id = 5"""

select_females = """SELECT name, age, nationality
FROM users WHERE gender = 'female'"""


 
# db_file_path = r"E:\Backup Files Abhinav_Satyam\Python\Python_Lec_practical_session\DailyPracticals\Day12_plotly\dbConnection\users.sqlite3"
db_file_path = "E:\\Backup Files Abhinav_Satyam\\Python\\Python_Lec_practical_session\\DailyPracticals\\Day12_plotly\\dbConnection\\users.sqlite3"

con = getConnection(db_file_path)



exec_query(con, create_table)
show(con)
exec_query(con, add_users)
show(con)
exec_query(con, update_user)
show(con)
exec_query(con, delete_user)
show(con)

exec_query(con, select_females)




con.close()
