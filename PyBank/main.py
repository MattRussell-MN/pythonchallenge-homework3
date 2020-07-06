# import os & poll_csv
import os
import csv

file_to_load = os.path.join("Resources", "budget_data.csv")
#voting_output = os.path.join("Output", "budget_table.txt")

#Define Variables

total_months = 0
total_pnl = 0
initial_pnl = 0
final_pnl = 0
average_change = 0
greatest_increase_month = 0
greatest_increase_revenue = 0
greatest_decrease_month = 0
greatest_decrease_revenue = -9999999999
total_change_pnl = 0
monthly_changes= []
profit = []
date = []

# Open the CSV file and read
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)

# Read the header
    header = next(reader)

# For each row in spreadsheet
    for row in reader: 

        #find total months
        total_months = total_months + 1

        #find total profit_loss
        profit.append(row[1])
        total_pnl = total_pnl + int(row[1])
        
        date.append(row[0])

        #find average monthly change in profit_loss
        final_pnl = int(row[1]) 
        monthly_change_profits = final_pnl - initial_pnl
        
        monthly_changes.append(monthly_change_profits)

        total_change_pnl = total_change_pnl + monthly_change_profits
        initial_pnl = final_pnl

        average_change = (total_pnl / total_months)
        
        #find greatest increase revenue value with greatest increase
        greatest_increase_revenue = max(monthly_changes)
        
        #find greatest decrease revenue value with 
        greatest_decrease_revenue = min(monthly_changes)

        #find month with greatest increase
        greatest_increase_month = date[monthly_changes.index(greatest_increase_revenue)]

        #find greatest decrease revenue value
        greatest_decrease_month = date[monthly_changes.index(greatest_decrease_revenue)]   
        

print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profits: " + "$" + str(total_pnl))
print(f"Average Change: {average_change}")
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase_revenue) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease_revenue) + ")")
    