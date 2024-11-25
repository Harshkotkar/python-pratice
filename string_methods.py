# str=input("enter the string:: ")
# result=len(str)  #len() method prints the length of the string
# result=str.find("a")  #find() method find the specific word,char from the stating of the sting and print the index position of the word,char.
#
# result=str.rfind("pizza") # rfind() method find the specific word,char from the reverse/last of the string and print the index position of the word,char.
#
# result=str.capitalize() #convert the first letter of the word,string into the capital
#
# result=str.upper() # conver the every letter of the sting into the uppercase
#
# result=str.lower() # convert the every letter of the string into the lowercase.
#
# result=str.isdigit() #will return true or false. if string contain only digits it will print true
#
# result=str.isalpha() # will return true or false. if string contains only the alphabetical character it will return true otherwise false
#
# result=str.islower() #will return truw if the string characters are in lower case otherwise false
#
# print(result)

# validate user input
#1. username is no more than 15 char
#2.must not contain spaces
#3.not contain digits
#
# username=input("enter the username::")
# if len(username)>15:
#     print("enter username less than 15 characters")
# elif " " in username:
#     print("username can not contain spaces")
# elif not username.isalpha():
#     print("username can not contain numbers")
# else:
#     print(f" Wellcome {username}");


# Validate a username according to the following criteria:
#
# The username must be greater than 6 characters and less than 12 characters.
# The first character must be an alphabet.
# It must contain at least one special character.
# It must contain at least one number.
# import re
#
# def valid(username):
#     if len(username)<=6 or len(username)>=15:
#
#         return False,"Username must be greater than 6 and less than 12"
#
#     if not  username[0].isalpha():
#         return False,"First char must be alphabet"
#
#     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', username):
#         return False,"Contain atleast one specal char"
#
#     if not any(char.isdigit() for char in username):
#         return False,"Must contain atleast one num"
#
#     return True,"Username valid"
# username=input("enter the username")
#
# valid,show=valid(username)
# print(show)


#indexing=accessing elements of a sequence using[] (indexing operator)
# [start:end:step]
#
# creditcard="1234-5678-9012"
# print(creditcard[0])
#
# print(creditcard[:4])
#
# print(creditcard[5:9])
#
# a="4"
# index=creditcard.find(a)
# print(index)
#
# print(creditcard[-1]) #[-1] will print the last number from string
# print(creditcard[::2]) #[::2] will print every second character in the string
#
# print(creditcard[-4:]) #return the last 4 digit of the string

#format specifier ={value:flag} format a value based on what flags are inserted

# price1=3.1234
# price2=-934.12
# price3=12.32
#
# print(f"price 1 is ${price1:.2f}")
#
# print(f"price 2 is ${price2:.3f}")
#
# print(f"price 3 is ${price3:.3f}")
#
#
# print(f"price 1 is ${price1:20}")
#
# print(f"price 2 is ${price2:20}")
#
# print(f"price 3 is ${price3:20}")
#
#
# print(f"price 1 is ${price1:>10}")
#
# print(f"price 2 is ${price2:>10}")
#
# print(f"price 3 is ${price3:>10}")
#
# print(f"price 1 is ${price1:<10}")
#
# print(f"price 2 is ${price2:<10}")
#
# print(f"price 3 is ${price3:<10}")
#
# print(f"price 1 is ${price1:^10}")
#
# print(f"price 2 is ${price2:^10}")
#
# print(f"price 3 is ${price3:^10}")





