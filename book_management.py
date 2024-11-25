import mysql.connector
from datetime import datetime
def connect_db():
    #Connect to MySQL database
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="books_db"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
def add_book(conn, title, author, read_before, pages):
    #Add a new book to the database
    date_added = datetime.now()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, read_before, pages, date_added, last_updated)VALUES (%s, %s, %s, %s, %s, %s)""", (title, author, read_before, pages, date_added, date_added))
    conn.commit()
    cursor.close()
    print("Book added successfully...!")


def lookup_book(conn, keyword):
    #Look up a book in the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s", (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    cursor.close()
    if results:
        for book in results:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Read: {book[3]}, Pages: {book[4]}, "
                  f"Date Added: {book[5]}, Last Updated: {book[6]}")
    else:
        print("No matching books found...")


def display_books(conn):
    #Display all books from the database.
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    if books:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Read: {book[3]}, Pages: {book[4]}, "f"Date Added: {book[5]}, Last Updated: {book[6]}")
    else:
        print("No books to display.")


def update_book(conn, book_id, title=None, author=None, read_before=None, pages=None):
    #Update an existing book in the database.
    cursor = conn.cursor()
    last_updated = datetime.now()

    # Prepare update statement dynamically
    fields_to_update = []
    values = []

    if title:
        fields_to_update.append("title = %s")
        values.append(title)
    if author:
        fields_to_update.append("author = %s")
        values.append(author)
    if read_before:
        fields_to_update.append("read_before = %s")
        values.append(read_before)
    if pages:
        fields_to_update.append("pages = %s")
        values.append(pages)

    if fields_to_update:
        fields_to_update.append("last_updated = %s")
        values.append(last_updated)
        values.append(book_id)

        query = f"UPDATE books SET {', '.join(fields_to_update)} WHERE id = %s"
        cursor.execute(query, tuple(values))
        conn.commit()
        print("Book updated successfully.")
    else:
        print("No fields to update.")

    cursor.close()

def del_book(conn,d_book):
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s ",(f"{d_book}", f"{d_book}"))
    result=cursor.fetchall()

    if result:
        print(f"{len(result)} result mathches the {d_book}")
        for i in result:
            print(f"ID: {i[0]}, Title: {i[1]}, Author: {i[2]}")
        confirm=input(f"Final conformation for deletion of the {d_book}?(Y/N) :").strip().lower()
        if confirm=="y":
            cursor.execute("DELETE FROM books WHERE title LIKE %s OR author LIKE %s ",(f"{d_book}", f"{d_book}"))
            conn.commit()
            print("Book deleted Successfully...!")
        else:
            print("Deletion cancelled")
    else:
        print(f"No book name {d_book} found in database...!")


    cursor.close()

def main():
    conn = connect_db()
    if not conn:
        print("Failed to connect to the database.")
        return

    while True:
        print("\n*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")

        print("4) Update a book")
        print("5) Delete the book")
        print("6) Quit")

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            print("Adding a book...")

            n_book = input("Enter the name of the book: ")
            n_author = input("Enter the name of the author: ")
            r_before = input("Have you read it before? (yes/no): ")
            n_pages = input("Enter the number of pages: ")
            while not n_pages.isdigit():
                print("Please enter a valid number for pages.")
                n_pages = input("Enter the number of pages: ")
            add_book(conn, n_book, n_author, r_before, int(n_pages))

        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter search term: ")
            lookup_book(conn, keyword)



        elif choice == 3:
            print("Displaying all books...")
            display_books(conn)

        elif choice == 4:
            print("Updating a book...")
            book_id = int(input("Enter the book ID to update: "))
            title = input("New Title (press Enter to skip): ")
            author = input("New Author (press Enter to skip): ")
            read_before = input("Read Before (yes/no, press Enter to skip): ")
            pages = input("New Pages (press Enter to skip): ")
            update_book(conn, book_id, title or None, author or None, read_before or None, pages if pages.isdigit() else None)



        elif choice==5:
            #delteting the book from the database
            print("Deleting the book...!")
            d_book=input("Enter the name/author of book:")
            del_book(conn,d_book)

        elif choice == 6:
            print("Exiting the program...")
            conn.close()
            break
        else:
            print("Invalid choice! Please make a choice between 1 to 5.")

    print("Program Terminated...!")


if __name__ == "__main__":
    main()
