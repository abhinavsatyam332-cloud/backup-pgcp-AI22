'''
Q.6
Following data displays min/max/average temp for cities
weather= [{'Mumbai' : [28, 30, 32]},.....]

1. Print the weather data
2. Print the city with maximum/min temp
3. Print all the cities that expereince min temp more than 30 degree
4. Create a dictionary to print 'City':'Ave temp'
'''


weather_data = [
    {"Mumbai": [28, 30, 32]},
    {"Delhi": [22, 25, 29]},
    {"Bengaluru": [20, 23, 26]},
    {"Kolkata": [27, 31, 33]},
    {"Chennai": [29, 32, 35]},
    {"pune": [31,34,36]}
]

print(weather_data)

min_max_temp = [ {city : {'min': min(temps) , 'max': max(temps)}}  for dic in weather_data           for city,temps in dic.items() ]
print(min_max_temp)

cities_experience_min_temp_more_than_30 = [city for dic in weather_data for city , temps in dic.items() if min(temps) > 30]
print(cities_experience_min_temp_more_than_30)

dict = [ {city: round(sum(temps) / len(temps) ,2 )} for dic in weather_data for city , temps in dic.items() ]
print(dict)