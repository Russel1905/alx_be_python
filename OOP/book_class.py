class Book:
    """A class to represent a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initialise a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when a Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation of the book for informal use."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a formal string representation of the book for debugging and recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
