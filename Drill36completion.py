'''
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)

Author: John Ossowski, Tech Academy Student (based in part on
the "Nice/Mean" game by Tech Academy Instructor Daniel A. Christie)

Purpose: This project will partially fulfill the requirements of Item 36 in the Python course.  It is a limited calculator that performs
operations on two variables with float values.
'''
def start(firstNum = 0, secondNum = 0, operation = "", answer = 0):
    firstNum, secondNum = getNums()
    operation = getOp()
    calculate(firstNum, secondNum, operation)
    exit()
    
#This function asks the user for two numbers and accepts float values.
def getNums():
    firstNum = float(input("First number please: "))
    secondNum = float(input("Second number please: "))
    return firstNum, secondNum

#This function asks the user to choose an operation.
def getOp():
    print("Choose an operation:\n Type 'a' for addition.\n Type 's' for subtraction.\n Type 'd' for division.\n Type 'm' for multiplication.\n Type 'i' to increase each number by 1.\n Type 'c' to decrease each number by 1.\n")
    operation = input("Your operation? ")
    return operation

#This function performs the operation and prints out the answer.
def calculate(firstNum, secondNum, operation):
    if(operation == "a"):
        sum = firstNum + secondNum
        answer = round(sum,2)
    elif(operation == "s"):
        difference = firstNum - secondNum
        answer = round(difference,2)
    elif(operation == "d"):
        quotient = firstNum / secondNum
        answer = round(quotient,2)
    elif(operation == "m"):
        product = firstNum * secondNum
        answer = round(product,2)
    elif(operation == "i"):
        firstNum += 1
        secondNum += 1
        firstInc = round(firstNum,2)
        secondInc = round(secondNum,2)
        answer = [firstInc, secondInc]
    elif(operation == "c"):
        firstNum -= 1
        secondNum -= 1
        firstDec = round(firstNum,2)
        secondDec = round(secondNum, 2)
        answer = [firstDec, secondDec]
    else:
        answer = "I don't recognize your operation."

    print("The result rounded to 2 decimal places is: {}".format(answer))

if __name__ == "__main__":
    start() 






            
