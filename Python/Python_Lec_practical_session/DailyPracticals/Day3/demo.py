colors_data = [
    {'Name': 'black', "rating": 50},
    {'Name':'Yellow', "rating":50},
    {'Name': 'blue', "rating": 80},
    {'Name': 'red', "rating": 90}
]

sorted(colors_data, key= lambda rat: rat['rating'])

print(colors_data)