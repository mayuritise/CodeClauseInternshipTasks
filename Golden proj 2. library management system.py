import qrcode 
import tkinter as tk
from tkinter import messagebox
import pickle
import os

class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies

    def decrease_available_copies(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def increase_available_copies(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:
            return False

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            for book in self.books:
                status = f"{book.available_copies}/{book.total_copies} available"
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")

    def add_user(self, user):
        self.users.append(user)

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def generate_qr_code(self, title):
        book = self.search_book(title)
        if book:
            qr_data = f"Title: {book.title}\nAuthor: {book.author}\nISBN: {book.isbn}"
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")
            qr_img.show()
        else:
            print("Book not found!")

def save_library_data(library):
    with open("library_data.pkl", "wb") as file:
        pickle.dump(library, file)

def load_library_data():
    if os.path.exists("library_data.pkl"):
        with open("library_data.pkl", "rb") as file:
            library = pickle.load(file)
        return library
    else:
        return Library()

def main():
    library = load_library_data()

    while True:
        print("\n---- Library Management System ----")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Add User")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Generate QR Code")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            total_copies = int(input("Enter the total number of copies: "))
            book = Book(title, author, isbn, total_copies)
            library.add_book(book)
            print("Book added successfully!")
            save_library_data(library)

        elif choice == "2":
            title = input("Enter the title of the book to remove: ")
            book = library.search_book(title)
            if book:
                library.remove_book(book)
                print("Book removed successfully!")
                save_library_data(library)
            else:
                print("Book not found!")

        elif choice == "3":
            title = input("Enter the title of the book to search: ")
            book = library.search_book(title)
            if book:
                status = f"{book.available_copies}/{book.total_copies} available"
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - {status}")
            else:
                print("Book not found!")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User(username, password)
            library.add_user(user)
            print("User added successfully!")
            save_library_data(library)

        elif choice == "6":
            username = input("Enter your username: ")
            user = library.get_user(username)
            if user:
                title = input("Enter the title of the book to borrow: ")
                book = library.search_book(title)
                if book:
                    if book.decrease_available_copies():
                        user.borrowed_books.append(book)
                        print(f"{book.title} borrowed successfully!")
                        save_library_data(library)
                    else:
                        print("All copies of the book are already borrowed.")
                else:
                    print("Book not found!")
            else:
                print("User not found!")

        elif choice == "7":
            username = input("Enter your username: ")
            user = library.get_user(username)
            if user:
                title = input("Enter the title of the book to return: ")
                book = library.search_book(title)
                if book:
                    if book.increase_available_copies():
                        user.borrowed_books.remove(book)
                        print(f"{book.title} returned successfully!")
                        save_library_data(library)
                    else:
                        print("All copies of the book are already returned.")
                else:
                    print("Book not found!")
            else:
                print("User not found!")

        elif choice == "8":
            title = input("Enter the title of the book to generate QR code: ")
            library.generate_qr_code(title)

        elif choice == "9":
            print("Exiting Library Management System.")
            save_library_data(library)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
