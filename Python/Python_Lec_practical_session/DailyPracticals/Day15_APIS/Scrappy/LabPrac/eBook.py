from LabPrac.book import Book


class EBook(Book):
    def __init__(self,title,author,price,file_size,is_borrowed=False):
        super().__init__(title,author,price,is_borrowed)
        self.file_size=file_size

    def __str__(self):
        return f'{super().__str__()}, File Size: {self.file_size}'
    def get_details(self):
        print(self.__str__())



