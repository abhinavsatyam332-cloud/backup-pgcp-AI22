import pandas as pd
import requests as req

res = req.get("https://jsonplaceholder.typicode.com/todos")

if res.status_code ==200:
    print("Success")


print("--------------------------------------------------")
data = res.json()
print(data)


print("--------------------------------------------------")
for obj in data:
    # print(obj['id'])
    if obj['userId'] == 1:
        print(obj['title'])


print("--------------------------------------------------")

user_ids = [('userId',4),('userId',7)]
res = req.get("https://jsonplaceholder.typicode.com/todos", params=user_ids)
if res.status_code == 200:
    print("Req success")
data = res.json()
print(data)



print("--------------------------------------------------")
prod_id = 7
res= req.get(f"https://jsonplaceholder.typicode.com/todos/{prod_id}")
data = res.json()
if res.status_code == 200:
    print("req success")
print(data)

print("--------------------------------------------------")
res = req.get("https://restful-booker.herokuapp.com/booking")
data = res.json()
if res.status_code == 200:
    print("req sucess")

for obj in data :
    print(obj['bookingid'])
print(data)