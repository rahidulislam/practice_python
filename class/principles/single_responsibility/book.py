class Book:
    def __init__(self,title:str, author:str,isbn:str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def add_to_library(self):
        print(f"Book {self.title} added to the library")

    def remove_from_library(self):
        print(f"Book {self.title} removed from the library")

    def generate_repot(self):
        print(f"Report: Book{self.title} by {self.author} (ISBN:,{self.isbn})")

# Instantiate the class
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book.add_to_library()
book.generate_repot()
book.remove_from_library()

# with SRP
class Book:
    def __init__(self, title:str, author:str,isbn:str):
        self.title = title
        self.author = author
        self.isbn = isbn

class LibraryManager:
    @staticmethod
    def add_to_library(book:Book):
        print(f"Book {book.title} added to the library")

    @staticmethod
    def remove_from_library(book:Book):
        print(f"Book {book.title} removed from the library")

class ReportGenerator:
    @staticmethod
    def generate_report(book:Book):
        print(f"Report: Book{book.title} by {book.author} (ISBN:,{book.isbn})")

# Instantiate the class
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
LibraryManager.add_to_library(book)
ReportGenerator.generate_report(book)
LibraryManager.remove_from_library(book)