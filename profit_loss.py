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