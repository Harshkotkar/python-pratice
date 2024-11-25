import random

options=['rock','paper','scissor']
player= None

computer=random.choice(options)
running=True

while running:
    player = None

    computer = random.choice(options)
    while player not in options:
        player=input("enter a choice (rock,paper,scissor) ::")

    print("player:", player)
    print("computer :", computer)

    if player==computer:
        print("match has been tie")
    elif player=="paper" and computer=="rock" or\
        player=="scissor" and computer=="paper" or\
        player=="rock" and computer=="scissor" :

        print("you win🤩🥳 ")
        if not input("play again (Y/N) ::").strip().lower() == 'y':
            print("Tata bye-bye sayonara alvidaaa goodbye😭")
            break

    else:
        print("computer win😭")

    print("keep playing untill you win🏆🥇")



