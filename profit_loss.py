from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"

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

def profit_loss():
    """
    - Function helps to calculate the net profit surplus or defecit
    - No parameters are required
    """
    # creating an empty list to store negative differences
    negative = []

    # for loop to loop rows from 1 to the number of sub list in data_list
    for row in range(1,len(data_list)):
        # calculating the difference between the net profit on the day itself and the day before
        difference = int(data_list[row][4]) - int(data_list[row-1][4])
       
        # if difference is negative, the day and the values of the difference would be exteneded in negative list
        if difference < 0:
            negative.extend([data_list[row][4],[difference]])
        # else programme will continue
        else:
            continue

        # if there are no values in the negative list, the programme will return a cash surplus
    if len(negative) == 0:
        return("[NET PROFIT SURPLUS] NET PROTIFT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

        # else it will return the day of the profit defecit and the amount of profit defecit in positive numbers
    else:
        # index will appear in even numbers and skip odd numbers
        for index in range(0,len(negative),2):
            return(f"[PROFIT DEFECIT] DAY: {float(negative[index])}, AMOUNT: USD{abs(negative[index+1])}")
