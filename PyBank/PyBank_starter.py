# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
last_month = 0
last_row = 0 
most_net_change = 0 
least_net_change = 0
net_change_li = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    for row in reader:
        #Track count of months
        total_months = total_months + int(row.count(row[0]))
        
        # Track the total
        total_net = int(row[1]) + (total_net)
        
        # Track the net change
        net_change = (int(row[1]) - (last_row))
        net_change_li.append(int(net_change))
       
        if net_change > most_net_change:
            most_net_change = net_change
            max_date = row[0]

        if net_change < least_net_change:
            least_net_change = net_change
            min_date = row[0]

        #Updating variable
        last_row = int(row[1])
# Calculate the average net change across the months
net_change_li.pop(0)
average_of_list = sum(net_change_li)
average = (average_of_list) / (total_months - 1)
#Max and Min calculations
max = max(net_change_li)
min = min(net_change_li)
# Generate the output summary
output =(
f"Financial Analysis\n"
f"--------------------\n"
f"Total Months: {total_months}\n"
f"Total: {int(total_net)}\n"
f"Average Change: {'%.2f'  % average}\n"
f"Greatest Increase In Profets: {max_date} ({max})\n"
f"Greatest Decrease In Profets: {min_date} ({min})\n")

# Print the output
print(output)
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
