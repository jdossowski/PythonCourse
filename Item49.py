'''
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)

Author: John Ossowski, Tech Academy Student (based on code found at:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
and http://python3.codes/popular-sorting-algorithms/

Purpose: Learning to code in Python!  (Item 49 in Python Course)
Write a program to sort a list.
'''

def start(aList = [], done = []):
    aList = getList()
    done = sortList(aList)
    print("Here is your sorted list: \n", done)
    exit()
    
def getList():
    print("This program will receive and sort a list of integers for you.\n")
    aList = []
    stop = True

    while stop:
        more = input("Do you have an integer to add to your list? Y or N: ").capitalize()
        if more == "Y":
            aListItem = int(input("Enter an integer please: "))
            aList.append(aListItem)
            stop = True
        elif more == "N":
            stop = False

    return aList

def sortList(aList):
    for passnum in range(len(aList)-1,0,-1):
        for i in range(passnum):
            if aList[i]>aList[i+1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]
    done = aList
    return done

if __name__ == "__main__":
    start()
