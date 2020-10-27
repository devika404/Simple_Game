#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


# In[ ]:


choice = ["Rock", "Paper", "Scissors"]
player = False
again=1
count_player=0
count_computer=0
while not player and again:
    computer=choice[random.randint(0,2)]
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
        print(" ")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            print(" ")
            count_computer=+1
        else:
            print("You win!", player, "smashes", computer)
            print(" ")
            count_player=+1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            print(" ")
            count_computer=+1
        else:
            print("You win!", player, "covers", computer)
            print(" ")
            count_player=+1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            print(" ")
            count_computer=+1
        else:
            print("You win!", player, "cut", computer)
            print(" ")
            count_player=+1
    else:
        print("That's not a valid play. Check your spelling!")
        print(" ")
    
    flag=1
    while flag:
        question = input("Do you want to play again? Y/N")
        print(" ")
        if question=='Y':
            player=False
            flag=0
        elif question=='N':
            player=True
            flag=0
        else:
            print("That's not an option, try again!")  
            print(" ")
if count_player>count_computer:
    print("You won more times than the computer!")
elif count_player<count_computer:
    print("You lost more times than the computer!")
else:
    print("You and the computer won the same number of times!")

