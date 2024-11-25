#standard way
list1=[]

for i in range(1,10):
    list1.append(i)
print(list1)

#mentos zindagi (using list comprehension)

list2=[i  for i in range(1,10)]
print(list2)

#square
sqr=[i**2 for i in range(1,11)]
print(sqr)

#cube
cube=[i**3 for i in range(1,11)]
print(cube)

#seprate the student marks above than 70

#standard way

marks=[67,89,68,76,78,91,96,55,44,67,56,64,66,43,49,51,56,78,77,72,74,65,63,65,53,59]
above=list(filter(lambda x:x>70,marks))
print(above)

scolar=[i if i>70 else "need improvement" for i in marks]
print(scolar)