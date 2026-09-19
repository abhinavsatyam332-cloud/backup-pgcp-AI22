'''

Q.8 Write a Python program to find the repeated items of a tuple.

'''

tp = (1,2,34,5,3,1,2)


tp = sorted(tp)
print(tp)
lst= []
for i in range(1,len(tp)):
    if tp[i] == tp[i - 1]:
        print("d")
        if tp[i] not in lst:
            lst.append(tp[i])
print(f"Repeated elements from {tp} are",lst)

