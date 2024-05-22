# Exercise 1 Introducing the list data type

## Defining a list

In this activity, you will edit a Python script to hold a collection of fruit names, or a list of fruit.

1. From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section.

2. In the file, enter the following code:

```bash
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
```

3. Save and run the file.

4. Confirm that the script runs correctly and that the output displays as you expect it to.

## Accessing a list by position

You can access the contents of a list by position. In this activity, you will print out each item in our list by their position:

5. In programming languages, the list position starts at zero (0). The brackets tell Python which position in the list you want. To access the apple string, enter the following code:

`print(myFruitList[0])`

6. To access the banana string, enter the following:

`print(myFruitList[1])`

7. To access the cherry string, enter the following code:

`print(myFruitList[2])`

8. Save and run the file.

9. Confirm that the script runs correctly and that the output displays as you expect it to.

## Changing the values in a list

The values of a list can be changed. In this activity, you will change cherry to orange.

10. In Python, list position starts at zero (0), so you must use the numeral 2 to access the third position. Enter the following code:

`myFruitList[2] = "orange"`

11. Print the updated list:

`print(myFruitList)`

12. Save and run the file.

13. Confirm that the script runs correctly and that the output displays as you expect it to.

```bash
['apple', 'banana', 'cherry']                                
<class 'list'>                                               
apple                                                        
banana                                                       
cherry                                                       
['apple', 'banana', 'orange'] 
```

# Exercise 2: Introducing the tuple data type

## Defining a tuple

The tuple is like a list, but it can't be changed. A data type that can't be changed after it's created is said to be immutable. To define a tuple, you use parentheses instead of brackets ([]).

14. Create a tuple by entering the following code:

```bash
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
```

15. Save and run the file.

16. Confirm that the script runs correctly and that the output displays as you expect it to.

## Accessing a tuple by position

Like a list, the items of a tuple can also be accessed by position:

17. To access the apple string, enter the following code:

`print(myFinalAnswerTuple[0])`

18. To access the banana string, enter the following code:

`print(myFinalAnswerTuple[1])`

19. To access the pineapple string, enter the following code:

`print(myFinalAnswerTuple[2])`

20. Save and run the file.

21. Near the top of the IDE window, choose the Run (Play) button.

22. Confirm that the script runs correctly and that the output displays as you expect it to.

```bash
['apple', 'banana', 'cherry']                                
<class 'list'>                                               
apple                                                        
banana                                                       
cherry                                                       
['apple', 'banana', 'orange']                                
('apple', 'banana', 'pineapple')                             
<class 'tuple'>                                              
apple                                                        
banana                                                       
pineapple
```

# Exercise 3: Introducing the dictionary data type

## Defining a dictionary

A dictionary is a list with named positions (keys). Imagine that your list shows people’s favorite fruit.

23. Return to the Python script, and enter the following code:

```bash
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
```

24. Use the print() function to write the dictionary to the shell:

`print(myFavoriteFruitDictionary)`

25. Use the type() function to write the data type to the shell:

`print(type(myFavoriteFruitDictionary))`

26. Save and run the file.

27. Confirm that the script runs correctly and that the output displays as you expect it to.

## Accessing a dictionary by name

In this activity, you will use the name of the individuals to get their favorite fruit, instead of numbers.

28. To access Akua's favorite fruit, enter the following code:

`print(myFavoriteFruitDictionary["Akua"])`

29. To access Saanvi's favorite fruit, enter the following code:

`print(myFavoriteFruitDictionary["Saanvi"])`

30. To access Paulo's favorite fruit, enter the following code:

`print(myFavoriteFruitDictionary["Paulo"])`

31. Save and run the file.

32. Confirm that the script runs correctly and that the output displays as you expect it to.

```bash
['apple', 'banana', 'cherry']                                
<class 'list'>                                               
apple                                                        
banana                                                       
cherry                                                       
['apple', 'banana', 'orange']                                
('apple', 'banana', 'pineapple')                             
<class 'tuple'>                                              
apple                                                        
banana                                                       
pineapple                                                    
{'Akua': 'apple', 'Saanvi': 'banana', 'Paulo': 'pineapple'}     
<class 'dict'>                                               
apple                                                        
banana                                                       
pineapple    
```

Congratulations! You have worked with the list, tuple, and dictionary data types in Python.
