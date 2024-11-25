import random
import string
import re


lst = [ "Iron Man", "Captain America", "Thor", "Hulk", "Black Widow", "Hawkeye",
    "Doctor Strange", "Spider-Man", "Black Panther", "Scarlet Witch", "Ant-Man",
    "Wasp", "Captain Marvel", "Star-Lord", "Gamora", "Drax", "Rocket Raccoon", "Groot",
    "Rapunzel","WALL-E","Buzz Lightyear","Woody","Elsa","Anna","Merida","Mirabel","Roz", ]

def username(length=1):
   w=random.sample(lst,length)
   word="".join(w)
   r_num=random.randint(2,5)
   new_word=' '.join([str(random.randint(0,9))for i in range(r_num)])
   semifinal_username=word+new_word
   final_username=re.sub(r'\s+','',semifinal_username)
   if re.fullmatch(r'[A-Za-z0-9]+',final_username):
       print(final_username)
   else:
       return username()


username()