import json
import random


# Custom exceptions
class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # Max 3 books allowed


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_from_file()

    def add_book(self, title, author):
        book_id = str(random.randint(1000, 9999))
        self.books[book_id] = Book(title, author)
        self.save_to_file()
        return book_id

    def add_member(self, name):
        member_id = str(random.randint(1000, 9999))
        self.members[member_id] = Member(name)
        self.save_to_file()
        return member_id

    def borrow_book(self, member_id, book_id):
        if book_id not in self.books:
            raise BookNotFoundException("Book not found in library.")
        if self.books[book_id].is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed.")
        if len(self.members[member_id].borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")

        self.books[book_id].is_borrowed = True
        self.members[member_id].borrowed_books.append(book_id)
        self.save_to_file()

    def return_book(self, member_id, book_id):
        if book_id not in self.books or book_id not in self.members[member_id].borrowed_books:
            raise BookNotFoundException("Book not found in member's borrowed list.")

        self.books[book_id].is_borrowed = False
        self.members[member_id].borrowed_books.remove(book_id)
        self.save_to_file()

    def save_to_file(self):
        data = {
            "books": {book_id: vars(book) for book_id, book in self.books.items()},
            "members": {member_id: vars(member) for member_id, member in self.members.items()}
        }
        with open("library_data.json", "w") as f:
            json.dump(data, f)

    def load_from_file(self):
        try:
            with open("library_data.json", "r") as f:
                data = json.load(f)
                self.books = {book_id: Book(**details) for book_id, details in data.get("books", {}).items()}
                self.members = {member_id: Member(details["name"]) for member_id, details in
                                data.get("members", {}).items()}
                for member_id, details in data.get("members", {}).items():
                    self.members[member_id].borrowed_books = details["borrowed_books"]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = {}
            self.members = {}


# Testing
library = Library()
book1 = library.add_book("1984", "George Orwell")
member1 = library.add_member("Alice")

try:
    library.borrow_book(member1, book1)
    print("Book borrowed successfully!")
    library.return_book(member1, book1)
    print("Book returned successfully!")
except Exception as e:
    print("Error:", e)
