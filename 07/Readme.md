# Python Conditional Statements Exercises

This repository contains exercises for learning and practicing Python conditional statements: `if`, `elif`, and `else`.

## Exercise 1: Working with the `if` statement

Working with the if statement In this exercise, you will edit a Python script to ship packages.

1. From the navigation pane of the IDE, choose the .py file that you created in the previous Creating your Python exercise file section.

2. Use the input() function to get information from the user:

`userReply = input("Do you need to ship a package? (Enter yes or no) ")`

3. Use the if statement to print a response.

The statements in an if statement are one tab indented from the if statement. In other programming languages, brackets are often used to indicate the start and end of a logic block, but Python uses spacing:

`if userReply == "yes": print("We can help you ship that package!")`

**Note:** The == symbol is a comparative operator. It means is equal to.

4. Save and run the file.

5. At the prompt, enter yes and press ENTER.

6. Confirm that you see a response.

7. Run the file again.

8. At the prompt, enter no and press ENTER. Confirm that the program exits and nothing id displayed.

## Exercise 2: Working with the `else` statement

To improve customer service, it would be nice to provide a reply even if the user doesn't want to ship a package. In this exercise, you will improve the Python script by using the else statement:

9. To handle the condition where the user doesn't want to ship a package, use the else statement:

`else: print("Please come back when you need to ship a package. Thank you.")`

10. Save and run the file.

11. At the prompt, enter no and press ENTER.

12. Confirm that you see a response.

13. Run the file again.

14. At the prompt, enter yes and press ENTER.

15. Confirm that you see a response.

## Exercise 3: Working with the `elif` statement

In this exercise, you will improve the Python script by offering the user additional services. When you have multiple conditions, you can use the elif statement, which is short for else-if.

    **Note:** The elif statement always comes after an if statement and before the else statement.

16. In the Python script, enter the following code:

```bash
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ") if userReply == "stamps": print("We have many stamp designs to choose from.") elif userReply == "envelope": print("We have many envelope sizes to choose from.") elif userReply == "copy": copies = input("How many copies would you like? (Enter a number) ") print("Here are {} copies.".format(copies)) else: print("Thank you, please come again.")
```

17. Save and run the file.

18. At the prompt, enter no and press ENTER.

19. Confirm that you see a response.

20. At the prompt, enter stamps and press ENTER.

21. Confirm that you see a response.

22. Run the file again.

23. At the prompt, enter yes and press ENTER.

24. Confirm that you see a response.

25. At the prompt, enter envelope and press ENTER.

26. Confirm that you see a response.

27. Run the file again.

28. At the prompt, enter no and press ENTER.

29. Confirm that you see a response.

30. At the prompt, enter copy and press ENTER.

31. Confirm that you see a response.

32. At the prompt, enter 2 and press ENTER.

33. Confirm that you see a response.

    **Note:** The if, elif, and else statements allow only one path to run at a time. The program doesn’t check the other statements after it finds a condition that is true.

As you can see, each time through the program had slightly different results. These differences demonstrate the power of conditionals.

Congratulations! You have written a Python script that uses `if`, `elif`, and `else` statements.