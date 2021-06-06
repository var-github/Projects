"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "local host",
    user = "user name"
    password = "password"
if we want to work with a particular database we have to mention
    database = "database name"
"""

# make database with python
"""
mycursor = mydb.cursor()
mycursor.execute("command name")
in this case mycursor.execute ("CREATE DATABASE pycheck")
"""

# to show databases
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
# print(x)

# how to create table inside a database with python
# customers is the name of the table
# mycursor.execute("CREATE TABLE customers with name which is a variable of length 255, address which is a variable")
# mycursor.execute("CREATE TABLE customers (name VARCHAR (255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)


# get info from a particular table
"""
mycursor.execute("SELECT * FROM table name")
myvalue = mycursor.fetchall()
for x in myvalue:
    print(x)
"""
# instead of fetchall if fetchone is used then it will show only one row
