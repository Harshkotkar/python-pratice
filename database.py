#python database connection pratice program to  perform the operation of insert update delete and alter operation on the database
#
# 1) Write a Python program for the following –
# a) Display information about the database.

import mysql.connector as mycon
mydb=mycon.connect(host="localhost",user="root",passwd="root",database="jdbc")

mycursor=mydb.cursor()


def dbs():
    mycursor.execute("show databases")
    print("DATABASE NAMES::")
    for i in mycursor:
        print(i)
# b) List of all tables in the database.

def tabels():
    print("TABLE NAMES ::")
    mycursor.execute("show tables;")
    tabel=mycursor.fetchall()
    print("table name ::",tabel)

dbs()
tabels()








