import mysql.connector


mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "nom11234",
	database = "codemydb2"
	)
#######################################
######Create A Cursor###################
my_cursor = mydb.cursor()

#######################################
######Create A Database###################

# my_cursor.execute("CREATE DATABASE codemydb2") #Function Create Database "codemydb2"
# Function to Create Database
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#	print(db[0])

#######################################
######Create A Table###################

#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#my_cursor.execute("SHOW TABLES")
#for table in my_cursor:
#	print(table[0])

sqlstuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("Norman", "dsvarietyhub@yahoo.com", 40)

my_cursor.execute(sqlstuff, record1)
mydb.commit()