# Import Modules 
import os
import csv


# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Set empty lists 
total_months = []
total_amount = []
profit_change = []
 
# Read in the CSV file

with open(csvpath, encoding="utf-8") as csvfile:

     # Split the data on commas
    csvreader = csv.reader(csvfile,delimiter=",") 

    # Skip the header
    header = next(csvreader)  

    #  Loop through the data
    for row in csvreader: 

        # Add the total_months and total_amount to their corresponding lists
        total_months.append(row[0])
        total_amount.append(int(row[1]))

    # loop through the total_amount to get the monthly change in profits
    for i in range(len(total_amount)-1):
        
        # Find the difference between two months and append to monthly profit change
        profit_change.append(total_amount[i+1]-total_amount[i])
        
# Find the max and min value for profit_change
max_increase_value = max(profit_change)
max_decrease_value = min(profit_change)

# Find max and min for the month 

max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1 


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Write to result file
result_file = os.path.join("Analysis","Financial_Analysis.txt")
with open(result_file,"w") as file:
    
# Put data  to Financial_Analysis file
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_amount)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")