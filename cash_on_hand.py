from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

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

def cash_on_hand():
    """
    -This function helps to calculate the cash surplus or cash defecit
    -No parameters are required
    """
    #creating an empty list to store negative differences
    negative = []
    
    # for loop to loop through the rows (1 to the numnber of sublist in data_list)
    for row in range(1,len(data_list)):
        # find the difference between cash on hand on the day and the cash on hand on the day before
        difference = (int(data_list[row][1])) - int(data_list[row-1][1])
        # when difference is negative, the day and the difference amount would be extended in the negative list
        if difference < 0:
            negative.extend([data_list[row][0],difference])
        # when difference is positive, the program will continue and the positive value will not be assigned to anything
        else:
            continue
    # if there is no values in negative list, program will return cash surplus
    if len(negative) == 0:
        return("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    
    # else it will return the cash defecit of the day itself and amount in positive numbers
    else:
        # the category will be even indexes will be category while the odd indexes are the values.
        for index in range(0,len(negative),2):
            return(f"[CASH DEFECIT] DAY: {float(negative[index])}, AMOUNT: USD{abs(negative[index +1])}")