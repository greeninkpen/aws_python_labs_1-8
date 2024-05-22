# assign string to variable myString
myString = "This is a string"
# print the string to console
print(myString)
# print data type of myString
print(type(myString))
# print value of myString and data type of myString
print(myString + " is of the data type " + str(type(myString)))

# assigns 2 strings to 2 variables 
firstString = "water"
secondString = "fall"
# concatenates the first 2 strings and assigns the result to a new variable
thirdString = firstString + secondString
# prints the value of the third string
print(thirdString)

# asks user for input and assigns the input to a variable
name = input("What is your name? ")
# prints the name the user entered
print(name)

# asks user for input of favorite color and animal
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
#prints a formatted string with the user's name, favorite color, and favorite animal
print("{}, you like a {} {}!".format(name,color,animal))