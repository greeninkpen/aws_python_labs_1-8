# Exercise 1: Creating a mixed-type list

You can mix data types in a Python list. In other languages, this capability is not a feature of lists. In this exercise, you will explore this capability.

1. From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section.

2. Define a list with different types, like the following example:

```bash
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
```

3. Use a for loop statement to traverse the list and print the data type for each item in the list:

```bash
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
```

4. Save and run the file.

5. Confirm that the script runs correctly and that the output displays as you expect it to.

```bash
45 is of the data type <class 'int'>                             
290578 is of the data type <class 'int'>                         
1.02 is of the data type <class 'float'>                         
True is of the data type <class 'bool'>                          
My dog is on the bed. is of the data type <class 'str'>          
45 is of the data type <class 'str'>
```

This exercise reinforced the Python programming concepts that were covered in labs 1–6. Although the code has only a few lines, it is powerful. Take some time to review the code and make sure you understand everything that happens in it.

Congratulations! You have worked with the list data type and learned about Python support for mixing data types in a list declaration.
