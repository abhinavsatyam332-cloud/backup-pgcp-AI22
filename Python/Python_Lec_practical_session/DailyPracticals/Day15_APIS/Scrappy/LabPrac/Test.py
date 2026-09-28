from LabPrac.book import Book
from LabPrac.eBook import EBook
from LabPrac.member import display_book_info, Member


class DuplicateBookError(Exception):
    pass


if __name__ == "__main__":
    # Instantiate Books
    b1 = Book("1984", "George Orwell", 15.99)
    e1 = EBook("Python 101", "Guido van Rossum", 29.99, 12.5)

    # Test Polymorphism
    print("--- Book Details ---")
    display_book_info(b1)
    display_book_info(e1)

    print("\n--- Borrowing & Returning Operations ---")
    m1 = Member(101, "Alice")

    # Borrowing books
    m1.borrow_book(b1)

    # Attempting to borrow an already borrowed book
    try:
        m1.borrow_book(b1)
    except DuplicateBookError as e:
        print(e)

    # Returning books
    m1.return_book(b1)