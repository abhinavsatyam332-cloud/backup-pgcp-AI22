import requests as req


print("----------------------------------------------")

header = {'Content-Type':'application/json'}
data = {
    "userId": 101,
    "id": 101,
    "title": "hello how are you",
    "body": "hello how are you"
  }

res = req.post("https://jsonplaceholder.typicode.com/posts",json = data, headers=header)
print(res.status_code)
res_data = res.json()
print(res_data)


# print(res_data['id'])

print("----------------------------------------------")

header = {'Content-Type':'application/json'}

payload = {
    "userId": 1,
    "id": 1,
    "title": "heyt",
    "body": "hey"
}

id = '1'
res = req.put(f"https://jsonplaceholder.typicode.com/posts/{id}",json=payload,headers = header)
print(res.status_code)


print("----------------------------------------------")

id = 3
header = {'Content-Type':'application/json'}
res = req.delete(f"https://jsonplaceholder.typicode.com/posts/{id}",headers=header)
print(res.status_code)
print(res.json())
