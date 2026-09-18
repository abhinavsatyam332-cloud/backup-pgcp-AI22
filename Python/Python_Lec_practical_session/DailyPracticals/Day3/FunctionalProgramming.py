from functools import reduce

from DailyPracticals.Day3.DemoDecorators import keep_time

books = [
    ["DSA", 1200],

    ["py for beginners", 800],
    ["Head first java", 1000]
]

change_case = list( map(lambda book: [book[0].title(), book[1]]  ,books) )
print(change_case)

greater_than = list( filter(lambda book: book[1]>900 ,books) )
print(greater_than)

sort_by_price = sorted(books, key=lambda book:book[1])
print(sort_by_price)

min_p = min(books, key=lambda book:book[1])
print(min_p)

colors_data = [
    {'Name': 'black', "rating": 50},
    {'Name':'Yellow', "rating":50},
    {'Name': 'blue', "rating": 80},
    {'Name': 'red', "rating": 90}
]

least_fev = min(colors_data, key=lambda dic: dic['rating'])
print(least_fev)

sort_by_rating = sorted(colors_data, key= lambda dic: dic['rating'])
print(sort_by_rating)

total_rating = reduce(lambda acc , curDic: acc + curDic['rating'], colors_data, 0)

print(total_rating)

rating_above_50 = list(filter(lambda dic: dic['rating'] > 50 , colors_data))
print(rating_above_50)