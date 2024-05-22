# assigns yes or no answer from user to var
userReply = input("Do you need to ship a package? (Enter yes or no) ")
# if userReply is yes, print the following
if userReply == "yes":
    print("We can help you ship that package!")
# if userReply is not yes, print the following
else:
    print("Please come back when you need to ship a package. Thank you.")

# assigns new question to userReply var for user to answer
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
# if elif else statement to check userReply
# if userReply is stamps, print the following
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
# if userReply is envelope, print the following
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
# if userReply is copy, print the following
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
# if userReply is not stamps, envelope, or copy, print the following
else:
    print("Thank you, please come again.")