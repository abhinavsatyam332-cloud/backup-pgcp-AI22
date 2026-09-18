def show(name):
    print(name)

def giveName(name):
    return name

def showstud(name,age):
    print(f'{name} : {age}')


def defaultArgs_showStud(name = 'user',age=18):
    print(f'{name} : {age}')

# defaultArgs_showStud("abhi",30)
defaultArgs_showStud(age=80)

def var_args_showStud(*args): # received tuple
    print(sum(args))

def var_kewargs(**kwargs):
    marks = kwargs['marks']
    return sum(marks)

var_args_showStud(12,34,56,34)
var_kewargs()