# nested loop = the inner loop will finish all of its iteration  before finishing one iteration of the outer loop
# rows=int(input("enter how many rows"))
# colums=int(input("how many colums"))
# symbol=input("enter symbol")
#
# for  i in range(rows):
#     for j in range(i+1):
#         print(symbol,end=" ")
#     print()
#
# 1 simple trangle pattern
# for i in range(0,5):
#      print('* '* (i+1))
#
# 2 inverred trangle
# for i in range(5,0,-1):
#     print("* "*i)
#
# 3 trangle
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# 4 inverted num trangle
# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# 5 inverted pyramid of *
# for i in range(6,0,-1):
#      print(" "*(5-i)+"* "*i)
#
# 6 pyramid
# print(" " )
# for i in range(1,6):
#     print(" "*(5-i)+"* "*i)
#
# 7 diamond pattern
#
# for i in range(1,6):
#     print(" "*(6-i)+"* "*i)
# for j in range(6,0,-1):
#     print(" "*(6-j)+"* "*j)
#
# 8 diamond patter num

for i in range(1,6):
    print(" "*(6-i)+" ".join(str(j) for j in range(1,i+1)))
for i in range(6,0,-1):
    print(" "*(6-i)+" ".join(str(j) for j in range(1,i+1)))

for i in range(1,6):
    for s in range(6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(6,0,-1):
    for s in range(6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()


def add(*args):
    sum=0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6))


