# 1. Data Types
# Easy:
# Question: Write a function convert_to_string(num) that takes an integer and returns it as a string.
#  Example:
#  convert_to_string(123) -> "123"

def convert_to_string(num):

    str1=str(num)

    print("before converting to string:",num,type(num))
    print("after converting to string:",str1,type(str1))
a=1234
# convert_to_string(a)

# Medium:
# Question: Write a function sum_mixed_list(lst) that takes a list of integers and strings, converts all elements to integers, and returns their sum.
#  Example:
#  sum_mixed_list(["10", 20, "30", 40]) -> 100


def sum_mixed_list(lst):
    sum=0
    for i in lst:
        s=int(i)
        sum +=s
    print("List:",lst)
    print("Total:",sum)
a=['1','2','3',4]
# sum_mixed_list(a)


# Hard:
# Question: Write a function group_by_type(data) that takes a list containing integers, floats, strings, and booleans and groups them by type into separate lists inside a dictionary.
#  Example:
#  group_by_type([1, 2.5, "hello", True, 3, 0.7]) -> {"int": [1, 3], "float": [2.5, 0.7], "str": ["hello"], "bool": [True]}

def group_by_type(data):
    dic={"int":[],"string":[],"bool":[]}

    for i in data:
        if isinstance(i,int) and not isinstance(i,bool):
             dic["int"].append(i)
        elif isinstance(i,str):
            dic["string"].append(i)
        elif isinstance(i,bool):
            dic["bool"].append(i)

    print(data)
    print(dic)

c=([1, 2.5, "hello", True, 3, 0.7])
# group_by_type(c)

# program to reverse the list elements
def reverse_list(lst1):

    print("list before :",lst1)
    lst1.reverse()
    print("list after",lst1)
d=["a","b","c"]
# reverse_list(d)

# Question: Write a function merge_dicts(d1, d2) that merges two dictionaries. If a key exists in both, the values should be added together.
#  Example:
#  merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) -> {"a": 1, "b": 5, "c": 4}

def merge_dict(d1,d2):
    print("d1:",d1)
    print("d2:",d2)
    d3=d1.copy()
    for key,value in d2.items():
        if key in d3:
            d3[key]+=value
        else:
            d3[key]=value
    return d3
# result=merge_dict({"a": 1, "b": 2}, {"b": 3, "c": 4})
# print("d3:",result)

from collections import Counter
def merge_dicts(dic1,dic2):
    print("dic1",dic1)
    print("dic2",dic2)
    dic3=Counter(dic1)+Counter(dic2)
    print(dict(dic3))
#merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})

# Question: Write a function find_unique_elements(lst) that takes a list and returns all unique elements in the order they first appear.
#  Example:
#  find_unique_elements([1, 2, 2, 3, 4, 1, 5]) -> [1, 2, 3, 4, 5]

def find_unique_elements(lst):
    set1=set(lst)
    lst1=[]

    for i in set1:
        lst1.append(i)
    print(lst1)

# find_unique_elements([1, 2, 2, 3, 4, 1, 5])

# Easy:
# Question: Write a function even_numbers(n) that returns all even numbers from 1 to n (inclusive).
#  Example:
#  even_numbers(10) -> [2, 4, 6, 8, 10]

def even_numbers(n):
    lst=[]
    for i in range(1,n+1):
        if i%2==0:
            lst.append(i)
    print(lst)

even_numbers(10)