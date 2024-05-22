# Exercise 1: Using the Python shell
In the terminal tab, a Python shell can be started by entering the following command:

`python3`

The Python shell should look similar to the following example.

```bash
Python 3.6.12 (default, Aug 31 2020, 18:56:18)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The three greater-than symbols (>>>) represent the prompt where the user can enter Python commands. In the following activities, you will practice using the Python shell by issuing some numeric commands.

## Adding

1. Enter the following input:

`2 + 2`

2. Press ENTER.
3. Confirm that you get 4 as output.

## Subtracting

4. Enter the following input

`4 - 2`

5. Press ENTER.

6. Confirm that you get 2 as output.

## Multiplying

To multiply, you use the * symbol:

7. Enter the following input:

`2 + 2`

8. Press ENTER.

9. Confirm that you get 4 as output.

## Dividing

To divide, use the / symbol:

10. Enter the following input:

`4 / 2`

11. Press ENTER.

12. Confirm that you get 2.0 as output.

## Exiting the Python shell

13. To exit the Python shell, enter the following command:

`quit()`

# Exercise 2: Introducing the int data type

To learn more about data types, you will use some built-in functions. A function is a piece of reusable code with a name. You use a function by:

* Calling by its name
* Including a list of one or more inputs called arguments, which are enclosed in parentheses
Python has several built-in functions that you can use to help you write more useful programs.

A collection of functions is called a library. Python’s collection of built-in functions is called the Python Standard Library.

## Editing a Python file

Instead of entering commands one by one in the Python shell, you will edit a text file that contains a sequence of commands:

14. From the navigation pane of the IDE, choose the file that you created in the previous Creating your Python exercise file section.

15. In the file, enter the following code:

`print("Python has three numeric types: int, float, and complex")`

16. To save the file, choose File > Save.

17. At the top of the IDE window, choose Run (the Play button).

18. In the bottom (console) pane of the IDE, confirm that the program prints the message: Python has three numeric types: int, float, and complex

**Note:** You might need to scroll up to see the console output.

19. In the terminal tab, you can also run the program by entering the following command, where <lab-python-file-name> is the name of the file that you created for this lab:

`python3 <lab-python-file-name>.py`

20. Confirm that the text you wrote is written to standard output.

```bash
~ $ python3 <lab-python-file-name>.py
Python has three numeric types: int, float, and complex
```

## Creating a variable

A variable is like a labeled box that stores information. You can change the contents of the box, but the label stays the same. In this activity, you will use the variable name myValue, but will store different data types in that labeled box.

21. Return to the Python file and on a new line, enter the following code:

`myValue=1`

22. Use the print() function to write the value of the variable to the shell. In the context of programming, writing means to add information to the shell.

`print(myValue)`

23. To get the data type of the variable, use the type() built-in function:

`print(type(myValue))`

24. To combine numbers and text, use the str() built-in function, which converts an argument into a collection of letters called a string. In this instance, you are converting the int (integer) data type into the string data type:

`print(str(myValue) + " is of the data type " + str(type(myValue)))`

25. Save the file.

26. To run the file, choose Run.

27. In the bottom pane of the IDE, confirm that you have the following output:

```bash
Python has three numeric types: int, float, and complex              
1                                                            
<class 'int'>                                                
1 is of the data type <class 'int'>                              
~ $
```
    **Note:** You might need to scroll up to see the output.


# Exercise 3: Introducing the float data type

The int data type only stores whole numbers. If you want to store a number with a decimal, like 3.14, you need a new data type called a float.

28. Return to the Python file and on a new line, enter the following code:

`myValue=3.14`

29. To write the value of the variable to the shell, use the print() function:

`print(myValue)`

30. Get the data type of the variable by using the type() built-in function:

`print(type(myValue))`

31. To combine numbers and text, use the str() built-in function:

`print(str(myValue) + " is of the data type " + str(type(myValue)))`

32. Save the file.

33. To run the file, choose Run.

34. In the bottom pane of the IDE, confirm that you see the following output:

```bash
Python has three numeric types: int, float, and complex              
1                                                            
<class 'int'>                                                
1 is of the data type <class 'int'>                              
3.14                                                         
<class 'float'>                                              
3.14 is of the data type <class 'float'>                         
~ $ 
```

    **Note:** Recall that you might need to scroll up to see the output.

# Exercise 4: Introducing the complex data type

In advanced math, an imaginary number is a complex number that can be written as a real number that is multiplied by the imaginary unit i. This complex data type is complicated because it must represent a letter and a number, such as 5j.

35. Return to the Python file and enter the following code:

`myValue=5j`

36. Write the value of the variable with the print() function:

`print(myValue)`

37. Get the data type of the variable with the type() function:

`print(type(myValue))`

38. To combine numbers and text, use the str() built-in function:

`print(str(myValue) + " is of the data type " + str(type(myValue)))`

39. Save the file.

40. To run the file, choose Run.

41. In the bottom pane of the IDE, confirm that you have the following output:

```bash
Python has three numeric types: int, float, and complex              
1                                                            
<class 'int'>                                                
1 is of the data type <class 'int'>                              
3.14                                                         
<class 'float'>                                              
3.14 is of the data type <class 'float'>                         
5j                                                           
<class 'complex'>                                            
5j is of the data type <class 'complex'>                         
~ $ 
```
    **Note:** Recall that you might need to scroll up to see the output.

# Exercise 5: Introducing the bool data type

The bool (Boolean) data type comprises the permanent names True and False, which are represented by the numerals 1 and 0, where 1 = True and 0 = False. The bool data type is implemented as a subset of int and is not considered a real data type. However, in some programming languages, it is implemented as a different data type. These exercises call the Python bool a fake data type.

42. Return to your text file, and enter the following code:

`myValue=True`

43. Write the value of the variable to the shell by using the print() function:

`print(myValue)`

44. Get the data type of the variable by using the type() built-in function:

`print(type(myValue))`

45. To combine numbers and text, use the str() built-in function:

`print(str(myValue) + " is of the data type " + str(type(myValue)))`

46. Save the file.

47. Choose Run (the Play button).

48. In the bottom pane of the IDE, confirm that it displays the correct output.

49. Return to your .py file and enter the following code:

`myValue=False`

50. Use the print() function to write the value of the variable to the shell:

`print(myValue)`

51. To get the data type of the variable, use the type() built-in function:

`print(type(myValue))`

52. To combine numbers and text, use the str() built-in function:

`print(str(myValue) + " is of the data type " + str(type(myValue)))`

53. Save the file.

54. Choose Run (the Play button).

55. In the bottom pane of the IDE, confirm that you have the following output:

```bash
Python has three numeric types: int, float, and complex              
1                                                            
<class 'int'>                                                
1 is of the data type <class 'int'>                              
3.14                                                         
<class 'float'>                                              
3.14 is of the data type <class 'float'>                         
5j                                                           
<class 'complex'>                                            
5j is of the data type <class 'complex'>                         
True                                                         
<class 'bool'>                                               
True is of the data type <class 'bool'>
False                                                         
<class 'bool'>                                               
False is of the data type <class 'bool'>                           
~ $
```

Congratulations! You have learned about Python’s three numeric data types: int, float, and complex. Additionally, you were introduced to the Python fake data type that is called bool. Note that bool is actually the numerals 0 and 1, which represent the values of True and False.
