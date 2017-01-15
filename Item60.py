'''
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)

Author: John Ossowski, Tech Academy Student 

Purpose: Learning to code in Python!  (Item 60 in Python Course)
Compare times in Portland, London and NYC to check if a business is open.
'''
import datetime

def start():
    PDXHour = getPDXTime()
    areTheyOpen(PDXHour)
    exit()

#Calculating the hour of the day in Portland.
def getPDXTime():

    now = datetime.datetime.now()
    PDXHour = now.hour
    return PDXHour

#Determining if London and NY are open based on Portland time.
def areTheyOpen(PDXHour):

    if PDXHour >=1 and PDXHour < 6:
        print("London branch is open.")
    elif PDXHour >= 6 and PDXHour < 13:
        print("London and NYC branches are open.")
    elif PDXHour >= 13 and PDXHour < 18:
        print("NYC branch is open.")
    elif PDXHour >=18 and PDXHour < 21:
        print("Only Portland is open now.")
    else:
        print("What are you doing at the office this late? Everyone is closed!")

if __name__ == "__main__":
    start()

