# # The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# # The greatest decrease in profits (date and amount) over the entire period


import os
import csv
from pprint import pprint

# Set path for file
csvdata = os.path.join("PyBank","Resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csvpath, 'r') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget_csv)
    data = [item for item in budget_csv]

month_count = 0
# Read through each row to count the month
for row in data:
    month_count += 1
print ("Financial analysis")
print ("-"*50)
print(f"Total number of months is: {month_count}")

# The net total amount of "Profit/Losses" over the entire period
total = 0
for x in data:
    total += int(x[1])
print (f"The net total is: {total}")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = []
months=[]
for a in range(1, len(data)):
    previous_value = int(data[a-1][1])
    current_value = int(data[a][1])
    
    change = current_value - previous_value
    changes.append(change)
# for the grestest change
    months.append(data[a][0])

# Change
if len(changes) > 0:
    average_change = round(sum(changes) / len(changes),2)
  
    greatest_change = max(changes)
    lowest_change = min(changes)

    greatest_change_month = months[changes.index(greatest_change)]
    lowest_change_month = months[changes.index(lowest_change)]
else:
    average_change = 0
    greatest_change = 0
    lowest_change = 0
    greatest_change_month = None
    lowest_change_month = None

print(f"Average Change: {average_change}")
print(f"Greatest Increase: {greatest_change_month} in {greatest_change}")
print(f"Greatest Decrease: {lowest_change_month} in {lowest_change}")

# Exporting to .txt file
to_file = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total number of months is: {month_count}\n"
    f"The net total is: {total}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase: {greatest_change} in {greatest_change_month}\n"
    f"Greatest Decrease: {lowest_change} in {lowest_change_month}\n"
)

textpath = os.path.join('PyBank', 'analysis', 'results.txt')
with open(textpath, 'w') as resultsfile:
    resultsfile.write(to_file)

