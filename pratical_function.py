#python program to create a user define function fact() accept a number and find the factorial of the number
def fact(n):
    if n==0 or n==1:
        return 1;
    else:
        result= n *fact(n-1)

        return result;
n=int(input("enter the value of  n"))
ans=fact(n)
print(ans)


