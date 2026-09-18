# Check if all letters in a string are uppercase

name="HELLO OL"
status = True
for ch in name:
    if(ch == ' '):
        continue
    if((ch >= 'A' and ch <= 'Z') or (ch >='0' and ch <='9')):
        pass
    else:
        status = False
        break


print(f'{name} : is in uppercase' if status else f'{name}: is not in uppercase')

