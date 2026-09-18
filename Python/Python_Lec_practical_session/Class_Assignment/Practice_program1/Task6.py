'''
Q 6. Create a list of books
e.g. booklist =[['Java 8', 700], ['Python for Beginners', 500],....]

Perform following operations on the list
1. Add a new book with price
2. Remove entry for a book
3. update price for a book
4. Sort the list by book names
5. Sort the list by prices
6. Print the book with max and min price [hint : you may use min()/max() functions of python]
'''

booklist = [    ['Java 8', 700],    ['Python for begineers', 500],
    ['Javascript',900],
    ['Machine Learning',2000]
]

# 1. Add a new book with price
booklist.append(['New book',200])
print("After adding ",booklist)

# 2. Remove entry for a book
booklist.remove(['Java 8', 700])
print("After removing ",booklist)

# 3. update price for a book
name_of_book_to_update_price = "Javascript"
new_price = 100
for book in booklist:
    if book[0] == name_of_book_to_update_price:
        book[1] = new_price
print(booklist)


# 4. Sort the list by book names
def getName(book):
    return book[0]
def getPrice(book):
    return book[1]

# 5. Sort the list by prices
booklist.sort(key=getName)
print(booklist)
booklist.sort(key=getPrice)
print(booklist)


# 6. Print the book with max and min price
print(min(booklist,key=getPrice))
print(max(booklist,key=getPrice))


