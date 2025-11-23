# main.py
from db import init_db
from users import add_student, update_student, delete_student, list_students
from books import add_book, update_book, delete_book, list_books
from issue_return import issue_book, return_book
from reports import issued_books, overdue_books, student_history

# Initialize DB on startup
init_db()

# --------------------------------------------
# Utility Functions
# --------------------------------------------

def print_records(records):
    if not records:
        print("\nNo records found.\n")
        return
    for row in records:
        print(dict(row))

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# --------------------------------------------
# Student Menu
# --------------------------------------------

def student_menu():
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            dept = input("Department: ")
            add_student(name, email, dept)
            print("Student added successfully!")

        elif choice == "2":
            sid = input_int("Student ID: ")
            name = input("New Name (Enter to skip): ") or None
            email = input("New Email (Enter to skip): ") or None
            dept = input("New Department (Enter to skip): ") or None
            update_student(sid, name, email, dept)
            print("Student updated!")

        elif choice == "3":
            sid = input_int("Student ID: ")
            delete_student(sid)
            print("Student deleted (if existed).")

        elif choice == "4":
            print_records(list_students())

        elif choice == "0":
            break

        else:
            print("Invalid choice!")


# --------------------------------------------
# Book Menu
# --------------------------------------------

def book_menu():
    while True:
        print("\n--- BOOK MANAGEMENT ---")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            category = input("Category: ")
            copies = input_int("Total Copies: ")
            add_book(title, author, category, copies)
            print("Book added!")

        elif choice == "2":
            bid = input_int("Book ID: ")
            title = input("New Title (Enter to skip): ") or None
            author = input("New Author (Enter to skip): ") or None
            category = input("New Category (Enter to skip): ") or None
            copies = input("New Total Copies (Enter to skip): ")
            copies = int(copies) if copies else None

            ok, msg = update_book(bid, title, author, category, copies)
            print(msg)

        elif choice == "3":
            bid = input_int("Book ID: ")
            delete_book(bid)
            print("Book deleted (if existed).")

        elif choice == "4":
            print_records(list_books())

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

# --------------------------------------------
# Issue & Return Menu
# --------------------------------------------

def issue_return_menu():
    while True:
        print("\n--- ISSUE / RETURN ---")
        print("1. Issue Book")
        print("2. Return Book")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input_int("Student ID: ")
            bid = input_int("Book ID: ")
            ok, msg = issue_book(sid, bid)
            print(msg)

        elif choice == "2":
            iid = input_int("Issue ID: ")
            ok, msg = return_book(iid)
            print(msg)

        elif choice == "0":
            break

        else:
            print("Invalid choice!")


# --------------------------------------------
# Reports Menu
# --------------------------------------------

def reports_menu():
    while True:
        print("\n--- REPORTS ---")
        print("1. View All Issued Books")
        print("2. View Overdue Books")
        print("3. View Student History")
        print("0. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            print_records(issued_books())

        elif choice == "2":
            print_records(overdue_books())

        elif choice == "3":
            sid = input_int("Student ID: ")
            print_records(student_history(sid))

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

# --------------------------------------------
# MAIN MENU
# --------------------------------------------

def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Student Management")
        print("2. Book Management")
        print("3. Issue / Return Books")
        print("4. Reports")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            book_menu()
        elif choice == "3":
            issue_return_menu()
        elif choice == "4":
            reports_menu()
        elif choice == "0":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
