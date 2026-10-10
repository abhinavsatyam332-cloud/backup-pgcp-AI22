''' 
longest subarray with sum k

 '''

arr = [1,45,56,3,23,56]
dic = {}
k = 57
for key, item in enumerate(arr):
    diff = k - item 
    if item in dic:
        print([dic[item], key])
        break

    dic[diff] = key
