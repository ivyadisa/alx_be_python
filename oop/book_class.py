# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: Returns a readable format of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Returns a string to recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
