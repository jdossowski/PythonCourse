#importing the randint function from random module
from random import randint

#defining a multiplication function
def multiplyBy5(x):
    return 5*x

#defining an addition function
def add5(x):
    return x+5

#defining a function to add a random number to another number
def randomAdd(x):
    #get random integer between 0 and 10
    #According to python.org - randint() Returns a random integer N such that a <= N <= b.
    y = randint(0,10)
    return x + y

