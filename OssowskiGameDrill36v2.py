'''
Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18)

Author: John Ossowski, Tech Academy Student (based on
the "Nice/Mean" game by Tech Academy Instructor Daniel A. Christie)

Purpose: This game is based on a simplified version of Pico, Fermi, Bagels - a 
number guessing game in which the player receives clues about the secret number
based on whether or not a guessed number shares digits with the secret number. 
For more information about Pico, Fermi, Bagels, see: http://www.math.washington.edu/~mathcircle/mmc/mmc2010/PicoFermiBagel.pdf
'''
#this initial conditions and plays the first round of the game (handling the case where the user guesses the number on the first try).
def start(name = "", secretNum = 0, secretNumOnes = 0, secretNumTens = 0, guess = 0, guessOnes = 0, guessTens = 0, winner = False):
    name = describe_game(name)
    secretNum, secretNumOnes, secretNumTens = secretNumGen()
    guess, guessOnes, guessTens = getUserGuess(name)
    winner = giveFeedback(guess, guessOnes, guessTens, secretNum, secretNumOnes, secretNumTens)
    if(winner):
        win(name, secretNum, secretNumOnes, secretNumTens, guess, guessOnes, guessTens)
    else:
        play(name, guess, guessOnes, guessTens, secretNum, secretNumOnes, secretNumTens, winner)

#the following function gets user's name (if name = "") and describes the game for the first time.
#this function was adapted from the nice/mean game developed by Tech Academy Instructor David A. Christie.
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
                        print("\nIn this game you will try to guess a two-digit number.")
                        print("\nAlong the way, I will tell you how well your guess matches the secret number.")
                        stop = False
    return name

#This function generates the secret number and gives the ones and tens places for comparison later in the game.
def secretNumGen():
    from random import randint
    from math import floor
    
    secretNum = randint(10,99) #gets a random two-digit number
    secretNumOnes = secretNum % 10 #gets the ones place
    secretNumTens = floor(secretNum / 10) #gets the tens place

    return secretNum, secretNumOnes, secretNumTens

#This function gets the user's guess and gives the ones and tens places for comparison later in the game.
def getUserGuess(name):
    guess = int(input("\nGuess a 2-digit number: "))  #gets a number from the user
    while guess < 10 or guess >= 100: #validating input, user must enter number between 10 and 99 inclusive.
        print("Sorry, {}, your guess needs to be a number between 10 and 99 inclusive.  Try again.".format(name))
        guess = int(input("\nGuess a 2-digit number: "))

    from math import floor
    guessOnes = guess % 10  #gets the ones place of the user's guess
    guessTens = floor(guess / 10) #gets the tens place of the user's guess

    return guess, guessOnes, guessTens

#This function gives the user feedback about how well their guess matched the secret number.        
def giveFeedback(guess, guessOnes, guessTens, secretNum, secretNumOnes, secretNumTens):

    #checking for some kind of match
    if guessOnes == secretNumOnes or guessTens == secretNumTens:
        someMatch = True
    elif guessOnes == secretNumTens or guessTens == secretNumOnes:
        someMatch = True
    else:
        someMatch = False

    #checking a special case where the user has guessed the ones and tens places of the secret number, but not the actual number.
    if guessOnes == secretNumTens and guessTens == secretNumOnes:
        reverseMatch = True
    else:
        reverseMatch = False

    #reporting back to the user about their guess (in case they guessed correctly, the win function will handle that notification).
    if guess == secretNum:
        winner = True
    elif someMatch == True and reverseMatch == False:
        print("\nYou're in luck.  One of your digits matches my number.")
        winner = False
    elif reverseMatch == True:
        print("\n Oooh!  You are so close!  You've got the right digits in the wrong places!")
        winner = False
    else:
        print("\nSo sorry, neither of those digits is in my number.")
        winner = False

    return winner

#This function continues game play until the user guesses the secret number.
def play(name, guess, guessOnes, guessTens, secretNum, secretNumOnes, secretNumTens, winner):
    while winner == False:
        guess, guessOnes, guessTens = getUserGuess(name)
        winner = giveFeedback(guess, guessOnes, guessTens, secretNum, secretNumOnes, secretNumTens)
    win(name, secretNum, secretNumOnes, secretNumTens, guess, guessOnes, guessTens)  

#This function indicates a win and asks user to play again.
def win(name, secretNum, secretNumOnes, secretNumTens, guess, guessOnes, guessTens):
    print("\nNice job {}, you guessed the secret number!".format(name))
    playAgain(name, secretNum, secretNumOnes, secretNumTens, guess, guessOnes, guessTens)

#Routine for checking to see if the user wants to play again, called in win function above.
def playAgain(name, secretNum, secretNumOnes, secretNumTens, guess, guessOnes, guessTens):
    stop = True
    while stop:
          choice = input("\n{}, do you want to play again? y/n ".format(name)).lower()
          if choice == "y":
              stop = False
              reset(name, secretNum, secretNumOnes, secretNumTens, guess, guessOnes, guessTens)
          if choice == "n":
              print("\nThanks for playing, {}!".format(name))
              stop = False
              exit()
          else:
              print("\nPlease enter 'y' for YES or 'n' for NO ...")

#Routine for resetting game if user wants to play game again (note: name is preserved).
def reset(name, secretNum, secretNumOnes, secretNumTens, guess, guessOnes, guessTens):
    secretNum = 0,
    secretNumOnes = 0,
    secretNumTens = 0,
    guess = 0
    guessOnes = 0,
    guessTens = 0,
    start(name, secretNum, secretNumOnes, secretNumTens, guess, guessOnes, guessTens)
           
if __name__ == "__main__":
    start() 






            
