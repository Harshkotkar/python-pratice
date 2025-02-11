#
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#
#     print("")

#
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print(" ")
#
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print(" ")
#
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#
#         print("*",end="")
#     print("")
#
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
# program to calculate area of rect and circle
#
# class circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14*(self.r**2)
# class rect:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
#
# obj1=rect(5,10)
# obj2=circle(3)
#
# print(f"area of circle={circle.area()}")
# print(f"area of rectangle={rect.area()}")

# Imagine you are managing a car rental service. Each car has a unique ID, a model name,and a daily rental rate.
# When a customer rents a car, they specify the number of days they want to rent it for.
# You need to calculate the total rental cost for the car based on the number of days rented and the daily rental rate.
#
# class cars:
#     def __init__(self, model_name, id, d_rate):
#         self.model_name = model_name
#         self.id = id
#         self.d_rate = d_rate
#
#     def __str__(self):
#         return f"unique id={self.id} model name={self.model_name} daily rate={self.d_rate}"
# class rent:
#     def __init__(self, car, rent_day):
#         self.car = car
#         self.rent_day = rent_day
#
#     def total_rent(self):
#         return self.car.d_rate * self.rent_day
#
#
# car1 = cars("Toyota Camry", "001", 50)
# rent1 = rent(car1, 3)
#
# print(car1)
# print(f"Total rental cost: {rent1.total_rent()}")


# def max(price):
#     profit=0
#     for i in range(1,len(price)):
#         if price[i]>price[i-1]:
#             profit+=price[i]-price[i-1]
#     return profit
#
# price=[7,1,5,3,6,4]
# print(max(price))

#
# def symmetry(s):
#     n=len(s)
#     h=n//2
#     if n%2==0:
#         return s[:h]==s[h:]
#     else:
#         return  s[:h] == s[h+1:]
#
# def palindrom(s):
#     return s==s[::-1]
#
# s1 = "khokho"
# s2 = "madam"
# print(f"{s1} is symmetrical: {symmetry(s1)}")
# print(f"{s1} is palindrome: {palindrom(s1)}")
# print(f"{s2} is symmetrical: {symmetry(s2)}")
# print(f"{s2} is palindrome: {palindrom(s2)}")



def swap(string_list):
    s_list = []
    for i in s_list:
        str = i.replace('G', '#').replace('e', 'G').replace('#', 'e')
        s_list.append(str)
    return s_list

list = ["Google", "Geek", "Green"]
final = swap(list)
print(final)















