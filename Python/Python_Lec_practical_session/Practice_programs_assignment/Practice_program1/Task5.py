'''
Q.5. Write a Python program to remove duplicates from a list
'''

lst= [1,2,3,4,56,3,2,1]
st = set(lst)
list_with_duplicates_removed = list(st)
print(list_with_duplicates_removed)