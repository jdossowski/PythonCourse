'''
Python: 3.5.2

Authored by: Daniel A. Christie, Instructor
Interpreted by: John Ossowski, Student

Purpose: Tech Academy Drill number 35, Python course.  This game demonstrates
how to pass variables from function to function.
'''

def start(nice = 0, mean = 0, name = ""): #initial conditions
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_OR_mean(nice, mean, name)

#the following function gets user's name (if name = "") and describes the game for the first time
def describe_game(name):
    if name != "":  #if name has a value, don't get name again, keep playing.
        print("\nThank you for playing again, {}".format(name))
    else:
            stop = True
            while stop: #this loop works to make sure user gives some input for name
                if name == "":
                    name = input("\nWhat's your name? ").capitalize()
                    if name != "":
                        print("\nWelcome, {}".format(name))
                        print("\nIn this game, you will be greeted by several different people. \nYou can be nice or mean.")
                        print("\nAt the end of the game, your fate will be influenced by your actions.")
                        stop = False
    return name

#this is the function responsible for the game play, it obtains user input about the choice to be nice or mean
def nice_OR_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? (n/m)").lower()
        if pick == "n":
            print("\nThey smile, wave and walk away...")
            nice+=1
            stop = False
        if pick == "m":
            print("\nThey scowl at you and stomp off...")
            mean+=1
            stop = False
    score(nice, mean, name)

#this function displays the user's nice and mean points
def show_score(nice, mean, name):
    print("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name, nice, mean))

#this function determines a win, loss or continued play based on points
def score(nice, mean, name):
    if nice > 5:
          win(nice, mean, name)
    if mean > 5:
          lose(nice, mean, name)
    else:
        nice_OR_mean(nice, mean, name)

#score will call this function if nice > 5, a win
def win(nice, mean, name):
    print("\nNice job {}, you win! \nEveryone loves you!".format(name))
    playAgain(nice, mean, name)

#score will call this function if mean > 5, a loss
def lose(nice, mean, name):
    print("\nToo bad {}, you lose! \nEveryone dislikes you intensely!".format(name))
    playAgain(nice, mean, name)

#in either a win or loss situation, the user is asked to if s/he wants to play again
def playAgain(nice, mean, name):
    stop = True
    while stop:
          choice = input("\n{}, do you want to play again? y/n ".format(name)).lower()
          if choice == "y":
              stop = False
              reset(nice, mean, name)
          if choice == "n":
              print("\nThanks for playing, {}!".format(name))
              stop = False
              exit()
          else:
              print("\nPlease enter 'y' for YES or 'n' for NO ...")

#if user wants to play game again, nice and mean are set to zero but name is perserved
def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)
              
if __name__ == "__main__":
    start() 






            
