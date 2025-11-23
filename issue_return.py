# issue_return.py
from db import get_connection
from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%d"

def issue_book(student_id, book_id):
    conn = get_connection()
    cur = conn.cursor()

    # Check availability
    cur.execute("SELECT available_copies FROM books WHERE book_id=?", (book_id,))
    book = cur.fetchone()

    if not book:
        return False, "Book not found."

    if book["available_copies"] <= 0:
        return False, "No copies available."

    issue_date = datetime.now()
    due_date = issue_date + timedelta(days=14)

    cur.execute("""
    INSERT INTO issues (student_id, book_id, issue_date, due_date)
    VALUES (?, ?, ?, ?)
    """, (student_id, book_id, issue_date.strftime(DATE_FORMAT), due_date.strftime(DATE_FORMAT)))

    cur.execute("UPDATE books SET available_copies = available_copies - 1 WHERE book_id=?", (book_id,))
    conn.commit()
    conn.close()
    return True, "Book issued successfully!"

def return_book(issue_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM issues WHERE issue_id=?", (issue_id,))
    issue = cur.fetchone()

    if not issue:
        return False, "Issue record not found."

    if issue["return_date"]:
        return False, "Book already returned."

    return_date = datetime.now().strftime(DATE_FORMAT)

    cur.execute("UPDATE issues SET return_date=? WHERE issue_id=?", (return_date, issue_id))
    cur.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id=?",
                (issue["book_id"],))

    conn.commit()
    conn.close()
    return True, "Book returned successfully!"
