from random import *
from difflib import SequenceMatcher
import time
def rps():
    global endmessage
    global draw
    global pwin
    global cwin
    name=raw_input("What's your name? ")
    if name=="":
        print("Ah, you'd rather remain anonymous, that's totally fine!")
        name="Player"
    else:
        name=name.capitalize()
    rps=["rock","paper","scissors"]
    draw="Draw!"
    computerlist=[]
    playerlist=[]
    pwin="You win!"
    cwin="I win!"
    erroroption="Error, you didn't select a valid option!"
    endmessage="You chose %s, and I had %s. "
    print("")
    print("Round one.")
    player=raw_input("Choose rock, paper, or scissors: ")
    player=player.lower()
    if player=="r" or similar(player,"rock") is True:
        player="rock"
    elif player=="p" or similar(player,"paper") is True:
        player="paper"
    elif player=="s" or similar(player,"scissors") is True:
        player="scissors"
    else:
        print(erroroption)
        return
    playerlist.append(player)
    computer=choice(rps)
    computerlist.append(computer)
    evaluate(player,computer)
    print("")
    print("Round two.")
    player=raw_input("Choose rock, paper, or scissors: ")
    player=player.lower()
    if player=="r" or similar(player,"rock") is True:
        player="rock"
    elif player=="p" or similar(player,"paper") is True:
        player="paper"
    elif player=="s" or similar(player,"scissors") is True:
        player="scissors"
    else:
        print(erroroption)
        return
    playerlist.append(player)
    computer=choice(rps)
    computerlist.append(computer)
    evaluate(player,computer)
    print("")
    print("Round three.")
    player=raw_input("Choose rock, paper, or scissors: ")
    player=player.lower()
    if player=="r" or similar(player,"rock") is True:
        player="rock"
    elif player=="p" or similar(player,"paper") is True:
        player="paper"
    elif player=="s" or similar(player,"scissors") is True:
        player="scissors"
    else:
        print(erroroption)
        return
    playerlist.append(player)
    computer=choice(rps)
    computerlist.append(computer)
    evaluate(player,computer)
    print("")
    print("Round four.")
    player=raw_input("Choose rock, paper, or scissors: ")
    player=player.lower()
    if player=="r" or similar(player,"rock") is True:
        player="rock"
    elif player=="p" or similar(player,"paper") is True:
        player="paper"
    elif player=="s" or similar(player,"scissors") is True:
        player="scissors"
    else:
        print(erroroption)
        return
    playerlist.append(player)
    computer=choice(rps)
    computerlist.append(computer)
    evaluate(player,computer)
    print("")
    print("Round five.")
    player=raw_input("Choose rock, paper, or scissors: ")
    player=player.lower()
    if player=="r" or similar(player,"rock") is True:
        player="rock"
    elif player=="p" or similar(player,"paper") is True:
        player="paper"
    elif player=="s" or similar(player,"scissors") is True:
        player="scissors"
    else:
        print(erroroption)
        return
    playerlist.append(player)
    computer=choice(rps)
    computerlist.append(computer)
    evaluate(player,computer)
    print("Round six, the hardest round to beat.")
    print("I am using an advanced array of algorithmic calculations to guess what you pick before YOU do. (not really)")
    player=raw_input("Go on, choose rock, paper, or scissors: ")
    player=player.lower()
    if player=="r" or similar(player,"rock") is True:
        player="rock"
    elif player=="p" or similar(player,"paper") is True:
        player="paper"
    elif player=="s" or similar(player,"scissors") is True:
        player="scissors"
    else:
        print(erroroption)
        return
    mostcommon=most_common(playerlist)
    if mostcommon=='rock':
        computer=='paper'
    elif mostcommon=='paper':
        computer=='scissors'
    elif mostcommon=='scissors':
        computer=='rock'
    playerlist.append(player)
    computerlist.append(computer)
    evaluate(player,computer)
    print "Nice playing, "+name+"!"
    
    


def evaluate(player,computer):
    if player=="rock" and computer=="rock":
        print endmessage % (player,computer) + draw
    if player=="rock" and computer=="paper":
        print endmessage % (player,computer) + cwin
    if player=="rock" and computer=="scissors":
        print endmessage % (player,computer) + pwin
    if player=="paper" and computer=="rock":
        print endmessage % (player,computer) + pwin
    if player=="paper" and computer=="paper":
        print endmessage % (player,computer) + draw
    if player=="paper" and computer=="scissors":
        print endmessage % (player,computer) + cwin
    if player=="scissors" and computer=="rock":
        print endmessage % (player,computer) + cwin
    if player=="scissors" and computer=="paper":
        print endmessage % (player,computer) + pwin
    if player=="scissors" and computer=="scissors":
        print endmessage % (player,computer) + draw



def similar(a, b):
    output=SequenceMatcher(None, a, b).ratio()
    if output>.5:
        return True
    else:
        return False


def most_common(playerlist):
    return max(set(playerlist), key=playerlist.count)
