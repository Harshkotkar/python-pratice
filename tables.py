import mysql.connector
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox


# MySQL database connection setup
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",  # Change to your MySQL password
            database="books_db"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Database connection failed: {err}")
        return None


def create_table():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                read_before VARCHAR(50),
                pages INT,
                date_added DATETIME,
                last_updated DATETIME
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()


# Function to add a new book
def add_book(title, author, read_before, pages):
    conn = connect_db()
    if conn:
        date_added = datetime.now()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO books (title, author, read_before, pages, date_added, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (title, author, read_before, pages, date_added, date_added))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Book added successfully!")


# Function to fetch all books from the database
def fetch_books():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        cursor.close()
        conn.close()
        return books


# Function to search for books
def search_books(keyword):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s",
                       (f"%{keyword}%", f"%{keyword}%"))
        books = cursor.fetchall()
        cursor.close()
        conn.close()
        return books


# Function to update an existing book
def update_book(book_id, title, author, read_before, pages):
    conn = connect_db()
    if conn:
        last_updated = datetime.now()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE books 
            SET title=%s, author=%s, read_before=%s, pages=%s, last_updated=%s 
            WHERE id=%s
        """, (title, author, read_before, pages, last_updated, book_id))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Book updated successfully!")


# GUI Application
class BookManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Manager")
        self.root.geometry("700x500")

        # Widgets for adding a book
        tk.Label(root, text="Title:").grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        tk.Label(root, text="Author:").grid(row=1, column=0)
        self.author_entry = tk.Entry(root)
        self.author_entry.grid(row=1, column=1)

        tk.Label(root, text="Read Before (yes/no):").grid(row=2, column=0)
        self.read_entry = tk.Entry(root)
        self.read_entry.grid(row=2, column=1)

        tk.Label(root, text="Pages:").grid(row=3, column=0)
        self.pages_entry = tk.Entry(root)
        self.pages_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=4, column=1, pady=10)

        # Widgets for displaying books
        self.tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Read", "Pages", "Date Added", "Last Updated"),
                                 show="headings")
        self.tree.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        self.refresh_books()

        # Search and update
        tk.Label(root, text="Search:").grid(row=6, column=0)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=6, column=1)
        self.search_button = tk.Button(root, text="Search", command=self.search_books)
        self.search_button.grid(row=6, column=2)

        self.update_button = tk.Button(root, text="Update Selected", command=self.update_selected_book)
        self.update_button.grid(row=7, column=1, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        read_before = self.read_entry.get()
        pages = self.pages_entry.get()

        if title and author and read_before and pages.isdigit():
            add_book(title, author, read_before, int(pages))
            self.refresh_books()
        else:
            messagebox.showerror("Error", "Please enter valid data.")

    def refresh_books(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        books = fetch_books()
        if books:
            for book in books:
                self.tree.insert("", tk.END, values=book)

    def search_books(self):
        keyword = self.search_entry.get()
        results = search_books(keyword)
        self.tree.delete(*self.tree.get_children())
        for book in results:
            self.tree.insert("", tk.END, values=book)

    def update_selected_book(self):
        selected = self.tree.focus()
        if selected:
            book_id = self.tree.item(selected, "values")[0]
            title = self.title_entry.get()
            author = self.author_entry.get()
            read_before = self.read_entry.get()
            pages = self.pages_entry.get()

            if title and author and read_before and pages.isdigit():
                update_book(book_id, title, author, read_before, int(pages))
                self.refresh_books()
            else:
                messagebox.showerror("Error", "Please enter valid data.")


# Main function to run the application
if __name__ == "__main__":
    create_table()
    root = tk.Tk()
    app = BookManagerApp(root)
    root.mainloop()
