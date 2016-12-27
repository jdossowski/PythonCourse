#dictionary defined and revised per Ch 12 and all lower case
epic_programmer_dict ={
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds' : ['lt@gmail.com', 333],
    'larry page' : ['lp@gmail.com', 444],
    'sergey brin' : ['sb@gmail.com', 555],
    }

userWantsMore = True

while userWantsMore == True:
#getting user input here
    personsName = input('Please enter a name: ').lower()

#getting person's info from dictionary (with additional try/except structure)
    try:
        personsInfo = epic_programmer_dict[personsName]
    #if no error then do the following
        print('Name: ' + personsName.title())
        print('Email: ' + personsInfo[0])
        print('Number: ' + str(personsInfo[1]))
    except:
    #if name entered doesn't match key in dictionary, then do the following
        print('No information found for that name. Please check spelling.')
    
    askUser = input('Would you like more info? (y/n) ')

    if askUser == 'y':
        userWantsMore = True
    elif askUser == 'n':
        userWantsMore = False
    else:
        print('Sorry, I don\'t understand that input.  Good-bye.')
        userWantsMore = False
        
