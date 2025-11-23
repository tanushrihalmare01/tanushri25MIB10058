# books.py
from db import get_connection
from models import fetch_books

def add_book(title, author, category, total_copies):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO books (title, author, category, total_copies, available_copies)
    VALUES (?, ?, ?, ?, ?)
    """, (title, author, category, total_copies, total_copies))
    conn.commit()
    conn.close()

def update_book(book_id, title=None, author=None, category=None, total_copies=None):
    conn = get_connection()
    cur = conn.cursor()

    # update total copies carefully
    if total_copies is not None:
        cur.execute("SELECT total_copies, available_copies FROM books WHERE book_id=?", (book_id,))
        book = cur.fetchone()
        diff = total_copies - book["total_copies"]
        new_available = book["available_copies"] + diff
        if new_available < 0:
            return False, "Cannot reduce copies below issued count."

        cur.execute("UPDATE books SET total_copies=?, available_copies=? WHERE book_id=?",
                    (total_copies, new_available, book_id))

    cur.execute("""
        UPDATE books SET 
            title=COALESCE(?, title),
            author=COALESCE(?, author),
            category=COALESCE(?, category)
        WHERE book_id=?
    """, (title, author, category, book_id))

    conn.commit()
    conn.close()
    return True, "Book updated!"

def delete_book(book_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE book_id=?", (book_id,))
    conn.commit()
    conn.close()

def list_books():
    return fetch_books()
