'''
Q1. Define a function overlapping () that takes two lists and returns True if they have at
least one member in common, False otherwise.
'''
def isOvelapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


if __name__ == "__main__":
    l1 = [2,4,6,8]
    l2 = [2,3,9,7]
    l3 = [10,11,12,23]
    print(isOvelapping(l1,l2))
    print(isOvelapping(l2,l3))