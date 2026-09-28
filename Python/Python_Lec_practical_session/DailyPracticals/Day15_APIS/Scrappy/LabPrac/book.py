

class Book:
    def __init__(self,title,author,price,is_borrowed=False):
        self.title=title
        self.author=author
        self.price=price
        self._is_borrowed=is_borrowed


    @property
    def is_borrowed(self):
        return self._is_borrowed
    @is_borrowed.setter
    def is_borrowed(self,value):
        self._is_borrowed=value

    def __str__(self):
        return f'Title:{self.title}, Author:{self.author}, Price:{self.price}, Borrowed:{self.is_borrowed}'

    def get_details(self):
        print(self.__str__())

