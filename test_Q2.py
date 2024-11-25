num=int(input("enter the number ::"));
print(num)
#to count the total digit in the given number
num_digit=len(str(abs(num)));
print(num_digit)

#prime number
n=11
for i in range(2,n):
    if n%i==0:
        break
if i==n-1:
    print("prime")
else:
    print("not prime");

f=0
s=1
print(f,s,end=" ")
for i in range(1,n-1):
    t=f+s
    print(t,end=" ")
    f=s
    s=t
























