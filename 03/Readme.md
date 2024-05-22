# Exercise 1: Introducing the string data type

A text file containing a logical sequence of commands is a script.

1. From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section.

2. In the file, enter the following code:

```bash
myString = "This is a string."
print(myString)
```

3. Save the file.

4. Run the file.

5. Confirm that the script runs correctly and that the output displays as you expect it to.

`This is a string.`

6. Extend the Python script by using the built-in function type() to get the data type of the variable. Enter the following code:

`print(type(myString))`

7. To convert the return value of type into a string, use the str() built-in function:

`print(myString + " is of the data type " + str(type(myString)))`

8. Save the file.

9. Run the file.

10. Confirm that the script runs correctly and that the output displays as you expect it to.

```bash
This is a string.
<class 'str'>
This is a string. is of the data type <class 'str'>
```

# Exercise 2: Working with string concatenation

String concatenation is the process of combining two strings into one string. You have actually been doing string concatenation since lab 1, but you didn’t call this process by that term. The plus sign (+) is used to concatenate strings. When the plus sign (+) is used with strings, it behaves differently than when you use it for numbers. In lab 1, you used the plus sign (+) to add numbers. Now, you will use the plus sign (+) to combine, or concatenate, strings.

11. Return to the Python script.

12. Create two strings and then concatenate them by entering the following code:

```bash
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
```

13. Save the file.

14. Run the file.

15. Confirm that the script runs correctly and that the output displays as you expect it to.

```bash
This is a string.                                            
<class 'str'>                                                
This is a string. is of the data type <class 'str'>
waterfall
```
​

# Exercise 3: Working with input strings

In coding, information that a user enters is known as input. You will use a built-in function named input() to get information from the user. The input() function will pause the code until a user enters a string and presses ENTER. Return to the Python script:

16. Enter the following code:

`name = input("What is your name? ")`

17. Use the print() function to write the value of the variable to the shell:

`print(name)`

18. Save the file.

19. Run the file.

20. Confirm that the script runs correctly and that the output displays as you expect it to.

```bash
This is a string.                                            
<class 'str'>                                                
This is a string. is of the data type <class 'str'>              
waterfall                                                    
What is your name? Maria                                     
Maria
```

# Exercise 4: Formatting output strings

When your script wants to communicate information back to the user, it is called output. You have been using the print() function to write output to the shell. You will create a survey and output the information that it collects back to the user.

21. Return to the Python script and enter the following code:

```bash
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
```

22. You have been using the print() function with only one variable, but you can also use it with multiple variables to format a string. Enter the following code:

`print("{}, you like a {} {}!".format(name,color,animal))`

23. Save the file.

24. Run the file.

The Python shell has stopped and is waiting for your input.

25. Enter a name and press ENTER.

26. Next, you are asked for your favorite color. Enter a color and press ENTER.

27. Next, you are asked for your favorite animal. Enter an animal and press ENTER.

28. Finally, the script prints a formatted string to the user by using the three pieces of information that you provided. Confirm that the output in the shell looks like the following output.

```bash
This is a string.                                            
<class 'str'>                                                
This is a string. is of the data type <class 'str'>              
waterfall                                                    
What is your name? Maria                                     
Maria                                                        
What is your favorite color?  blue                           
What is your favorite animal?  dog                           
Maria, you like a blue dog!  
```
    **Note:** The final print() statement uses the format() function. In the format() function, the opening and closing braces ({}) act as placeholders for the variables that will be passed to (that is, put between) the function's parentheses.

Congratulations! You have used Python to concatenate strings, take input from the user, and output a formatted string.