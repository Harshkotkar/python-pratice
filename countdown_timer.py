import time

my_time=int(input("enter time in sec:"))

for i in range(my_time,0,-1):
    print(i)
    time.sleep(1)
print("times up")