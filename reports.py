# reports.py
from db import get_connection
from datetime import datetime

def issued_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT i.issue_id, s.name AS student, b.title AS book,
           i.issue_date, i.due_date, i.return_date
    FROM issues i
    JOIN students s ON i.student_id = s.student_id
    JOIN books b ON i.book_id = b.book_id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def overdue_books():
    today = datetime.now().strftime("%Y-%m-%d")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM issues 
    WHERE return_date IS NULL AND due_date < ?
    """, (today,))
    rows = cur.fetchall()
    conn.close()
    return rows

def student_history(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT issues.issue_id, books.title, issues.issue_date, issues.due_date, issues.return_date
    FROM issues
    JOIN books ON issues.book_id = books.book_id
    WHERE student_id=?
    """, (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows
