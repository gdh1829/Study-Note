#!python

a = [1,2,3]

iterater = iter(a)
for i in iterater:
    print(i, end='\n')

def printFunc(first, second, third):
    return first, second, third

print(printFunc(second=3, first=1, third=5))

a = input("any number?")
print(a)