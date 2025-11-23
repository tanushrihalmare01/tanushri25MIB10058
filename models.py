# models.py
from db import get_connection
from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d"

# ---------------- STUDENTS ----------------
def fetch_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_student_by_id(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    row = cur.fetchone()
    conn.close()
    return row

# ---------------- BOOKS ----------------
def fetch_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def fetch_book_by_id(book_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE book_id=?", (book_id,))
    row = cur.fetchone()
    conn.close()
    return row
