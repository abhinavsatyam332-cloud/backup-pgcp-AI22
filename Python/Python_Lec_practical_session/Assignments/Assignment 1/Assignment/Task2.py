start = 2
end = 10

print(f"Prime numbers between {start} and {end}:")

for i in range(start, end):
  if i > 1:
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      print(i)