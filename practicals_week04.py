import math
from math import log2

print(math.sqrt(2401))
print(math.log2(1024))

def displayTwice(msg):
    '''This function displays a message twice.'''
    print(msg)
    print(msg)

displayTwice("Hello there!")
displayTwice("Second message!")
help(displayTwice)

def findMax(a,b):
    """Finds the maximum of two values."""
    if ( a > b ):
        max = a
    else:
        max = b
    return max

print(findMax(10, 5))
print(findMax(2, 100))

def multiplyNumbers(a,b = ""):
    if b != "":
        return a * b
    else:
        return a * a

print(multiplyNumbers(10, 5))
print(multiplyNumbers(10))

def someFunc(x, y, z):
    print("x is", x, "\ny is", y, "\nz is", z)

someFunc(1, 2, 3)
someFunc(z=3, x=1, y=2)

print("This", "is", "a", "message", sep="m")
print("This is", "another message", sep="??")

def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num

    return total/len(numbers)

print(calcAve(50, 20))

hypot = lambda a,b : math.sqrt(a * a + b * b)
print(hypot(3,4))
print(type(hypot)) # returns 'function'

to_seconds = lambda hours, minutes = 0 : (hours * 3600) + (minutes*60)
print(to_seconds(0, 2))
print(to_seconds(2, 0))
print(to_seconds(1, 30))
print(to_seconds(1))