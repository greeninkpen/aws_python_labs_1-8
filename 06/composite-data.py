# imports module to read csv files
import csv
# imports module to make deep copy of files 
import copy

# creates dictionary with key/value pairs for car details
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# loop that iterates through the myVehicle dictionary and prints a formatted str
# with the key and value
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
# creates empty list for inventory to later be added to 
myInventoryList = []

# function to open, read, and close csv file when finished 
# and extract data from car_fleet.csv
with open('car_fleet.csv', 'r') as csvFile:
    # dictates how data will be read and assigned to csvReader
    csvReader = csv.reader(csvFile, delimiter=',')  
    # var used to initializes a count starting at 0
    lineCount = 0  
    # for loop to extract column names from csvReader file
    for row in csvReader:
        # conditional to test if lineCount contains Column headings yet
        if lineCount == 0:
            # fprint string stating column names separated by commas
            print(f'Column names are: {", ".join(row)}')  
            # increments lineCount by 1
            lineCount += 1  
        else: 
            # fprint string stating vin, make, model, year, range, topSpeed, zeroSixty, and mileage 
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            # creates a deep copy of myVehicle dictionary
            currentVehicle = copy.deepcopy(myVehicle)  
            # assigns values to the keys in the currentVehicle dictionary
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            # appends currentVehicle with new data to myInventoryList
            myInventoryList.append(currentVehicle)  
            # increments lineCount by 1
            lineCount += 1  
    # fprint string stating how many lines were processed
    print(f'Processed {lineCount} lines.')

# for loop to iterate through myInventoryList and print key/value pairs
for myCarProperties in myInventoryList:
    # for loop to iterate through myCarProperties dictionary
    for key, value in myCarProperties.items():
        # fprint string stating key and value
        print("{} : {}".format(key,value))
        # fprint string to separate each row of data
        print("-----")