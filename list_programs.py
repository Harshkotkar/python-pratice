# Addition of the values of the list
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

list3=[x+y for x,y in zip(list1,list2)]
print(list3)

#using for loop
list4=[]
for i in range(len(list1)):
    list4.append(list1[i]+list2[i])
print(list4)

#using while loop
list5=[]
i=0
while i<len(list1):
    list5.append(list1[i]+list2[i])
    i+=1
print(list5)

#reversing the list using built in function
#reverse()
list1.reverse()
print(list1)

#reversed()
reversed_list=list(reversed(list2))
print(reversed_list)
#slicing
reversed2_list=list3[::-1]
print(reversed2_list)



x = 1
y = 2
z = x
x = y
y = z
print(x, y)

x = int(input())
y = int(input())

x = x % y
x = x % y
y = y % x

print(y)



