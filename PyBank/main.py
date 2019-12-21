# import dependencies
import csv
import sys

# csv file path
budget_data = "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv"


months = []
profits = []

# open and read file
with open(budget_data, newline='') as csvfile:
    sys.stdout = open('final.txt', 'w')

    csvreader = csv.reader(csvfile, delimiter=',')

    # skips header
    csv_header = next(csvreader)

    # variables and placeholders
    totalMonths = 0
    profit = [1]
    total_profit = 0
    total_loss = 0
    netPL = 0
    total_amount = 0
    pl_change = []
    # loop to find total months and net amount for profits/losses
    for row in csvreader:
        
        totalMonths = totalMonths + 1
        total_amount = total_amount + int(row[1])

        months.append(row[0])
        profits.append(int(row[1]))


greatest_inc = [1][0]
greatest_dec = [1][0]

# loop to find greatest increase in profits and decrease in profits
for r in range(len(profits)):
    if profits[r] >= greatest_inc:
        greatest_inc = profits[r]
        great_inc_month = months[r]
    elif profits[r] <= greatest_dec:
        greatest_dec = profits[r]
        great_dec_month = months[r]
# find average change to 2 decimal places
average_change = round(total_amount / totalMonths, 2)

# prints final output
final_print = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {great_inc_month} (${greatest_inc})\n"
    f"Greatest Decrease in Profits: {great_dec_month} (${greatest_dec})"
)

print(final_print)