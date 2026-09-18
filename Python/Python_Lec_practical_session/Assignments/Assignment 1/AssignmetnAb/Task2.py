start = 1
end = 97

pnum = 1
print(f"Prime numbers between {start} and {end}")

for i in range(start ,end+1):
    if i%2 == 0:
        continue
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        print(i)