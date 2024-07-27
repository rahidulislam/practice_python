class Book:
    """
    Exercise 1: Basic Class and Object

    Task: Create a class called Book that has the following attributes and methods:

        Attributes:
            title (string)
            author (string)
            pages (integer)

        Methods:
            __init__(self, title, author, pages): Initializes the attributes.
            description(self): Returns a string describing the book in the format "Title by Author, X pages".

    Challenge: Create an instance of the Book class and print its description.
    """

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")


# =================================================================

b1 = Book("Python", "Guido van Rossum", 400)
b1.description()
