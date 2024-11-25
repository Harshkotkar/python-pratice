#compond interest

# principle=0
# rate=0
# time=0
#
# while True:
#     principle=float(input("Enter the principle amount:"))
#     if principle<=0:
#         print("Principle can not be less than or equal to zero")
#     else:
#         break
#
# while True:
#     rate=float(input("Enter the intrest rate:"))
#     if rate<=0:
#         print("Intrest rate can not be less than equal to zero")
#     else:break
# while True:
#     time=int(input("Enter the time in years:"))
#     if time<=0:
#         print("Time can not be less than or equal to zero")
#     else:
#         break
#
#
# total=principle*pow((1+rate/100),time)
#
# print(f"Balance after {time} year's: ${total:.2f}")

#guess the number game

import random as rnd

num=rnd.randint(0,100)
guess=None
print("Type exit at any time to quit the game.")
while True:
    guess=input("Guess the number btn 1 to 100::")
    if guess.lower()=="exit":
        print("Yor are exiting the game tata,byebye")
        break

    try:
        guess=int(guess)
        if guess<0 or guess>100:
            print("Enter the number btn 0 to 100")
            continue

    except ValueError:
        print("Enter the valid number or type exit to leave the game")
        continue

    if guess <num:
        print(f"number is lower  try again")

    elif guess > num:
        print(f"number is heigher  try again")

    else:
        print("Congratulations :) you guess the correct number......")
        break