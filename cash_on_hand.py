from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"

#reading mode to rede csv file
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
    