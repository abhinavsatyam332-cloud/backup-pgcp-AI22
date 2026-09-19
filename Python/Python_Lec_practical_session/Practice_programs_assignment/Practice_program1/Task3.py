# nm = "Was it a rat I saw? or Dammit, I'm mad!"

nm =input("Enter string to check it is palindrome or not: ")
nm = nm.upper()

name = str([ch for ch in nm if ch >='A' and ch<='Z'])

palindrome= True
left=0
right=len(name)-1

while left<right:
    if name[left]!=name[right]:
        palindrome=False
        break
    else:
        pass

    left+=1
    right-=1

if palindrome:
    print("Given string is palindrome")
else:
    print("Not a palindrome")
