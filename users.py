# users.py
from db import get_connection
from models import fetch_students

def add_student(name, email, department):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, email, department) VALUES (?, ?, ?)",
                (name, email, department))
    conn.commit()
    conn.close()

def update_student(student_id, name=None, email=None, department=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students 
        SET name=COALESCE(?, name),
            email=COALESCE(?, email),
            department=COALESCE(?, department)
        WHERE student_id=?
    """, (name, email, department, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    conn.commit()
    conn.close()

def list_students():
    return fetch_students()
