from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

#reading mode to read csv file
with fp.open(mode = "r",encoding = "UTF-8", newline ="") as file:
    
    #instantiate a reader object
    reader = csv.reader(file)
    next(reader)
    
    #creating empty data_list to store all the raw data
    data_list = []
    
    #appending each line from reader to data_list
    for line in reader:
        data_list.append(line)

# creating list to store overheads values and the highest overheads
overheads_list = []
highest = []

def overheads():
    """
    - Finds out the highest overheads
    - No parameters are required
    """

    # for loop to append data from overheads value to overheads list
    for row in range(len(data_list)):
        overheads_list.append(float(data_list[row][1]))
   
    # sort the overheads values in ascending order
    overheads_list.sort()

    # for loop to loop through the row numbers of the data_list
    for row in range(len(data_list)):
        
        # using overhead values from raw data to find out which category matches the highest overheads(-1 index)
        if float(data_list[row][1]) == overheads_list[-1]:
            
            # when matched it will append the category and value from raw data to the highest list
            highest.append(data_list[row])
        else:
            # else programme will continue
            continue

    # return the category in capital words and its value of the overheads
    return(f"[HIGHEST OVERHEADS] {highest[0][0].upper()}: {highest[0][1]}%")       

