from LabPrac.DuplicateBook import duplicate, BookNotFound

class Member:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            raise duplicate("The give book is already borrowed")
        book.is_borrowed = True
        self.__borrowed_books.append(book)
        print(f'{self.__name}, {book.title}')


    def return_book(self, book):
        if book in self.__borrowed_books:

            book.is_borrowed=False
            self.__borrowed_books.remove(book)
        else:
            raise BookNotFound("Not Borrowed")


def display_book_info(book):
        book.get_details()