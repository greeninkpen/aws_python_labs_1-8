# Creates a list of mixed data types
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
# Iterates through the list and prints a string for each item with its data type
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))