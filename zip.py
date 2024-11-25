username=["spiderman","ironman","captain america"]
password=["peter","tony","stive"]

user=zip(username,password)
for i in user:
    print(i)

#2 into list,

user1=list(zip(username,password))
for i in user1:
    print(i)
print(type(user1))

#3 dictonary
user2=dict(zip(username,password))
for key,value in user2.items():
    print(key+":"+value)
print(type(user2))

#4
last_login=["12-10-2021","17-09-2019","08-05-2019"]

user3=list(zip(username,password,last_login))
for i in user3:
    print(i)
    