import functools

letters=["h",'e','l','l','o']
word=functools.reduce(lambda x,y:x+y,letters)
print(word)

num=[]
for i in range(1,10):
    num.append(i)
print(num)

factorial=functools.reduce(lambda x,y:x*y,num)

print(factorial)



w="Mr.smoothi is the ben 10's favriout drink"
a=w.split()
print(a)