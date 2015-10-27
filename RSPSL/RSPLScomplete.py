#!/usr/bin/env python
#previous line tells unix to use python to run... using env gets the location of python.

# Rock Paper Scissors Lizard Spock Game
import random
numName = ['rock','spock','paper','lizard','scissors']
winDict={'rock': ['breaks','mashes'], 'spock': ['vaporizes','takes apart'], 'paper': ['disproves','covers'], 'lizard':['eats','poisons'],'scissors':['decapitates','cuts up']}
playerChoice = str()
computerChoice = str()


def Player_Interface(): 
    #Player interface portion of the game
    while True:
        global playerChoice

        print"\n\n Type your choice: rock, Spock, paper, lizard or scissors"
        playerChoice = raw_input(" (or QUIT to stop):")
        
        if playerChoice == "QUIT":
            break
        if playerChoice == "spock" :
            print "Commander Spock was an officer of Starfleet!!!"
            print "He definitely counts as a proper noun! Try Again!"
            continue
        if (playerChoice in numName) or playerChoice.lower() in numName:
            playerChoice=playerChoice.lower()
            numName[1]=numName[1].lower()
            print Win_Logic((numName.index(playerChoice.lower())))
        else:
            print playerChoice, " is not one of the options! Try Again!"


def Win_Logic(key1):
    #Game logic
    global computerChoice

    key2 = random.randrange(5)
    numName[1]=numName[1].capitalize()
    computerChoice = numName[key2]
    playerChoice =numName[key1]
    winCal=(key1-key2) % 5

    resultString = "\nYou chose %s.\nThe computer chose %s.\n%s %s %s.\n%s"
    numName[1]=numName[1].capitalize()

    if winCal == 0:
        return "You and the computer both chose " + computerChoice + ".\nIt's a tie!"
    elif winCal >=3:
        if winCal == 4:
            winCal = 0
        if winCal == 3:
            winCal = 1
        action = winDict[computerChoice.lower()][winCal]
        return resultString % (playerChoice,  computerChoice, computerChoice.capitalize(), action, playerChoice, "You lose.")
    else:
        winCal = (winCal-1)
        
        action = winDict[playerChoice.lower()][winCal]
        return resultString % (playerChoice,  computerChoice, playerChoice.capitalize(), action, computerChoice, "You win.")

Player_Interface() #Run Game