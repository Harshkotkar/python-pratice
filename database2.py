# 2)Write a Python program to connect a database and create the following table within the database.
# Product (product_id, product_name, rate, quantity)


import mysql.connector

conn = mysql.connector.connect( host="localhost",user="root",password="root",database="jdbc")

cursor = conn.cursor()
def create():
    str1 = "CREATE TABLE Product1 ( product_id INT PRIMARY KEY, product_name VARCHAR(50),rate FLOAT, quantity INT);"
    cursor.execute(str1)
    print("Product table created successfully")


# 3)Write a Python program to insert 5 records -in the Product table and display all the records
def insert_data():
    insert = "INSERT INTO Product1 VALUES (%s, %s, %s, %s)"

    products = [
        (101, 'Laptop', 80000.0, 5),
        (102, 'Macbook', 90000.5, 3),
        (103, 'Phone', 35000.0, 4),
        (104, 'PS5', 55000.0, 5),
        (105, 'Earbuds', 6500.0, 6) ]

    cursor.executemany(insert, products)
    conn.commit()

    print(f"{cursor.rowcount} records inserted successfully.")

    cursor.execute("SELECT * FROM Product")
    records = cursor.fetchall()

    print("All records in the Product table:")
    for row in records:
        print(row)

# 4)Write a program to update the rate of the product with product_id 105 in the Product table. using mysql
def update_data():
    update = "UPDATE Product1 SET rate = %s WHERE product_id = %s"
    new_rate = 135.0
    product_id = 105

    cursor.execute(update, (new_rate, product_id))
    conn.commit()

    print(f"Rate of product with ID {product_id} updated successfully.")

    cursor.execute("SELECT * FROM Product WHERE product_id = 105")
    record = cursor.fetchone()
    print("Updated record:", record)
create()
insert_data()
update_data()