###########################################################
# Learn Python Coding In 2019
# By Norman Morgan
# dsvarietyhub.com
#############################################################


# Clear The Terminal or Screen
import os
os.system('clear')

##############################################################
# ############DATA TYPES############
# 1 - Strings = has "" mark
# 2 - Numbers = NO "" mark
# 3 - Lists = (A List can be edited) (Starts at ZERO) (List has[])
# 4 - Tuples = (a list that can not be edited) (Tupples has ()  )
# 6 - Dictionaries = ( have a key and a value paired with that key) (Has {})
# 7 - Boolean = (True or False)
##############################################################



#full_name = 'Norman Morgan'
# print (full_name)
#age = 40  # numbers (Has no "")
# names = ("John", "Mary", "Bob") # Lists and tupples 
# print (names[2])

# fav_pizza = {
#	"Norman Morgan": "Extra Cheese",
#	"Mary": "Sausage",
#	"Bob": "Baccon"
# }
# print (fav_pizza["Bob"])

# name = True
################################################################
# Lesson #9 Starts Hear 

#greetings = "Hello, My name is Norman Morgan"


#print (greetings.split(" ")[4:6])
################################################################
#######Lesson #10 Statrs Here#######Numbers And Math############

#num = 10
#print(float(num))
#####################
#num = 10.50
#print(int(num))
#####################
#print(10%3)  #Return The Remainder of Division
#print(5**3)
#print(10/3)
#print(7*3)
#print(7-3)
#print(7+3)
#####################
#num_1 = 10
#num_2 = 10
#print(num_1 * num_2)

#print(4 + 1 * 3) #order of opperation multiplication done 1st
#print((4 + 1) * 3) #order of opperation () done 1st

#num = "5"
#print((int(num)) * 3) 
###############################################################
#####Lesson #11 Start Here##List##############################

#other_name = "Zack"
#nums = [1, 2, 3, 4, 5]
#names = ["Morgan", "John", "Mary", nums] #this is a list inside a list
#print(names[3][2] + 10)
#names = ["Morgan", "John", "Mary", 55] #this is a list (Start fro Zero)
#names[1] = "Brook" ## replace the value of [1] with brook
#names.append("brook") ## adds "brook" to end of the list
#print(names)
#################################################

#names = ["Morgan", "John", "Mary"]

#print(len(names))
#print(names[len(names)-1]) #Print the Last Value in List
#####################################################3
#####Lesson #12 ###Topples#####

#names = ("Morgan", "John", "Mary") #Tuples Has ()
#print(names[0])

#tuple1 = ("Morgan", "John", "Mary")
#tuple2 = ("Green",)
#tuple3 = tuple1 + tuple2

#print(tuple3)
#########################
#tuple1 = ("Morgan", "John", "Mary")
#tuple2 = ("Green",)

#print(tuple1[0:2])
###########################
#tuple1 = ("Morgan", "John", "Mary")
#tuple2 = ("Green",)
#tuple3 = tuple1[0:2]
############################################
##### Dictionaries 13 (has 2 values a key)

#fav_movies = {
#	"James": "X-Men",
#	"Smith": "Spiderman",
#	"Kimberly": "Girl on The Train",
#	"Peter": "Barbershop",
#	"Kevin": "Wolverine",
#	"John": "Back To The Future"
#}

#del fav_movies["John"] # DELETE Value From Dictionary
#print(fav_movies) # Print entire Dictionary
#fav_movies.update({"Stewart": "Superman"}) # This is to add new entry to the dictionary
#fav_movies["James"] = "Deadpool"
#print(fav_movies) # Print a specific record from the dictionary "" 

####################################################
###Lesson  #15 Comparison Operators############
# Comparison Operator = True Or False 
			#######################
			#     ##Operators##   #
			# ==                  #
			# !=                  #
			# >                   #
			# <                   #
			# >=                  #
			# <=                  #
			#######################

print(10 == 10)
# /C/Users/nemes/Documents/My_Files/MyCodes/PytonProjects/PythonTT