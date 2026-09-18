def calculate_discount(x):
    return x * 0.85

#
# books = [
#     {"py for beginners": 800},
#     {"Head first java": 1000},
#     {"DSA": 1200}
# ]
#
# discounted_p = {
#      k:calculate_discount(v)
#
#     for book in books
#     for k, v in book.items()
# }
# print(discounted_p)



books = {
    1: {"py for beginners": 800},
    2: {"Head first java": 1000},
    3: {"DSA": 1200}
}

discounted_p = {
     title:calculate_discount(price)

    for k,v in books.items()

    for title,price in v.items()
}

print(discounted_p)




#
#
# book1 = {"py for beginners": 800,
#          "Head first java": 1000,
#          "DSA": 1200}
#
# discounted2_p = { calculate_discount(vv) for kk,vv in book1.items()}
# print(discounted2_p)
