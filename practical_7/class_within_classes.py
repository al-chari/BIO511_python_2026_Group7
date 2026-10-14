# Create the class Book, with the proper attributes
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrower = None

    def __str__(self):
        # The __str__ dunder method will be called when using print(book_obj)
        return(f"Informative message about the book. You can also use attributes {self.title}")

# Create the class Book
class Library:
    def __init__(self):
        # I found it more logical to create two different lists. One for availables and another one for non-available ones.
        self.available_books = []
        self.non_available_books =[]

    # If a book is added, we add it to the list and change its availability to True.
    def add_book(self, book):
        self.available_books.append(book)
        book.available = True
        return self.available_books

# Create the class Member
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    # If we want to borrow a book, we first need to see if it is available.
    def borrow_book(self, library, book):
        if book.available == True:
            # Then we must add it to the borrowed books list for the member, remove it from the library available book list, and add it to the non-available list.
            self.borrowed_books.append(book)
            library.available_books.remove(book)
            library.non_available_books.append(book)
            book.available = False
            # We also must add the name of the borrower.
            book.borrower = self.name

        


# Example usage
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
library = Library()
library.add_book(book1)  # Should add book1 to the library and make it available for borrowing
library.add_book(book2)
member1 = Member("Alice")
member1.borrow_book(library, book1)  # Now the book should be borrowed by Alice
print("Available books:", [str(book.title) for book in library.available_books])
print("Non available books:", [str(book.title) for book in library.non_available_books])
