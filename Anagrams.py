# str1=input("enter str1")
# str2=input("enter str2")
#
# if len(str1)!=len(str2):
#     print("not anagrams")
# else:
#     if sorted(str1)==sorted(str2):
#         print("anagrams")
#     else:
#         print("not anagrams")

#valid anagram
import random
str1=input("enter the str1 ")
lst=list(str1)
random.shuffle(lst)
str2="".join(lst)
print(str1,"\n",str2)

if len(str1)!=len(str2):
    print("no anagrams")
else:
    if sorted(str1)==sorted(str2):
        print("anagrams")
    else:
        print("not anagram")