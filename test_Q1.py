# # Accespt the sentence from user
# sentence =input("enter the sentence =")
#
# #display the alternarte character
# alter_char=sentence[::2]
# print(alter_char)
#
# # extract word using list and dispay the list
#
# words=sentence.split()
# print(words)
#
# # convert all words into uppercaase
#
# Upper_word= [x.upper() for x in words]
# print(Upper_word)
#
# # create a new string and check the existing.....
#
# new_str=input("enter the new  string ")
#
# if new_str in sentence:
#     print("yes,'{new_str}' is present in the sentence")
# else:
#     print(f"no,{new_str} is present in the sentence")

#area of rectangle
# len=int(input("enter the length"))
# width=int(input("enter the width"));
# area=len*width;
# print(area);

#shoping cart program
# item=input("what u want to buy ");
# price=float(input("enter the price "));
# quantity=int(input("quantity please "));
# total=price*quantity
# print(f"u have bought {quantity} X {price}");
# print(f'total is{total}');

# madlibs game
# madlibs is a game where you create a story
# by fillling in the blanks using the random words

# arithmatics and mathematics
# circle operations
import math
# radius=float(input("enter the radius of circle"));
# circumference=2*math.pi*radius;
# print("cercumference= ",circumference)
#
# area=math.pi*pow(radius,2);
# print("area=",area)
#hipotanus of rectangle
# a=float(input("enter side A"))
# b=float(input("enter side B"))
# c=math.sqrt(pow(a,2)+pow(b,2))
# print("hypotanus of rectangle",c)

#calculator
# while True:
#     num1=int(input("Enter the fist number:: "));
#     num2=int(input("Enter the second number:: "));
#     print("1)Additon\n2)Substraction\n3)Multiplication\n4)Division\n5)Exit")
#     operator=int(input("Enter the operation to be performe:: "));
#     if operator==1:
#         print(f"Addition of {num1} & {num2} = ",num1+num2);
#     elif operator==2:
#         print(f"Substraction of {num1} & {num2} = ",num1-num2);
#     elif operator==3:
#         print(f"Multipication of {num1} & {num2} = ",num1*num2);
#     elif operator==4:
#         if num2!=0:
#          print(f"Division of {num1} & {num2} = ",num1/num2);
#         else:
#             print("Error:Division by zero is not allowed.....")
#     elif operator==5:
#         print("Exiting.....tata,bye-bye.");
#     else:
#         print("Invalid input....")
#
#     retry=input("Do U want to try again (yes/no):: ").strip().lower();
#     if retry!="yes":
#         print("Exiting.....tata bye-bye");
#         break

#weight converter
while True:
    weight=int(input("Enter Ur weigth:: "))
    unit=input("Killograms or Pounds? (K or P orrr Exit)").upper()

    if unit=="K":
        weight *= 2.205
        unit="Pound"
    elif unit=="P":
        weight /=2.205
        unit="Kg"
    elif unit=="EXIT":
        print("Exiting.....tata,bye-bye.")
    else:
        print(f"{unit} was not valid")
    print(f"Your weight is {round(weight,1)} {unit}")

    retry = input("Do U want to try again (yes/no):: ").strip().lower();
    if retry!="yes":
        print("Exiting.....tata,bye-bye.")
        break





