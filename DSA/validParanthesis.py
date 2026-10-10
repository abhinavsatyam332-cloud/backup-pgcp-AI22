
# optimized
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        stack = [] # ind to remove

        for i,ch in enumerate(arr):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack and arr[stack[-1]] == '(':
                    stack.pop()
                else:
                    arr[i] = ''
        
        while stack:
            arr[stack.pop()] = ''
        
        return ''.join(arr)


    

# o(n^2)  time complexity
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] 
        arr2 = list(s)
        torem = []

        for ind,ch in enumerate(s):
            if ch == '(':
                stack.append(ch)
            
            if len(stack) == 0 and ch == ')':  
                torem.append(ind)
            
            if stack and stack[-1] == '(' and ch == ')':
                stack.pop()

            
        for i in torem:
            arr2.pop(i)

        if len(stack) > 0:
            while(len(stack) > 0):
                arr2.pop()
                stack.pop()