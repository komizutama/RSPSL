# Rock Paper Scissors Lizard Spock Game

name_to_number = {"rock" : 0, "spock" : 1, "paper" : 2, "lizard" : 3, "scissors": 4}
oChoice = str()

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"



def rpsls(player_choice):

    print "\n"


    print "You chose " + oChoice + "."

    pNum = name_to_number[player_choice]


    cNum = random.randrange(5)

    cChoice = number_to_name(cNum)

    print "The computer chose " + cChoice + "."


    wincal = (pNum-cNum) % 5

    if wincal >= 3:
        print cChoice + " beats " + oChoice + "!"
        print "The computer wins!"
    elif wincal >=1:
        print pChoice.lower() + " beats " + cChoice + "!"
        print "You win!"
    else:
        print "It's a tie!"

import random
pChoice = str()
while True:
    print"\n\nType your choice: rock, Spock, paper, lizard or scissors"
    pChoice = raw_input(" (or QUIT to stop):")
    oChoice = pChoice

    
    if pChoice == "spock" :
        print "Commander Spock was an officer of Starfleet!!!"
        print "He definitely counts as a proper noun! Try Again!"
        continue
    else:
        pChoice = pChoice.lower()
        if pChoice == "quit":
            break
        elif pChoice in name_to_number:
            rpsls(pChoice)
        else:
            print pChoice, " is not one of the options! Try Again"
            continue
