'''
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)

Author: John Ossowski, Tech Academy Student (based in part on
the "Nice/Mean" game by Tech Academy Instructor Daniel A. Christie)

Purpose: This program partially fulfills the requirements of item 36 of the Python course.
It first asks the user to define the length of his/her grocery list and accepts itesm on the list.
Then it eturns a random snarky comment about each item on the list.
'''
def start(grocList = []):
    grocList = getList()
    giveSnark(grocList)
    exit()

#This function gets the list of groceries.  Can we change range to be whatever length user specifies?
def getList():
    grocList = []
    start = 0
    step = 1
    end = int(input("How many items are on your list? "))

    def my_range(start, end, step):
        while start < end:
            yield start
            start += step

    for x in my_range(start,end, step):
        item = input("Enter an item on your grocery list: ")
        grocList.append(item)

    return grocList

#This function returns the list with a random snarky comment for each item.
def giveSnark(grocList):
    from random import randint
    snarkTuple = ["Really??", "Do you think you need that?", "Would this break your new year's resolution?", "Are you sure you know how to cook this?", "You're not worried about cholesterol, right?"]
    for item in grocList:
        snarkIndex = randint(0,4)
        print(item + " - " + snarkTuple[snarkIndex])
        
if __name__ == "__main__":
    start() 






            
