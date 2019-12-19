import os
import csv
import sys

budget_data = os.path.join("PyBank/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

months = []
revenue = []

with open(budget_data, newline='') as csvfile:
    sys.stdout = open('final.txt', 'w')

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    totalMonths = 0
    profit = [1]
    total_profit = 0
    total_loss = 0
    netPL = 0
    totalRevenue = 0
    pl_change = []

    for row in csvreader:
        
        totalMonths = totalMonths + 1
        totalRevenue = totalRevenue + int(row[1])

        months.append(row[0])
        revenue.append(int(row[1]))

#    print(f"Total Months: {totalMonths}")
#    print(f"{totalRevenue}")

greatest_inc = [1][0]
greatest_dec = [1][0]

for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]

#print(f"{great_inc_month} {greatest_inc}")
average_change = round(totalRevenue / totalMonths, 2)
#print(f"{average_change}")
#print(f"{great_dec_month} {greatest_dec}")

final_print = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${totalRevenue}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {great_inc_month} (${greatest_inc})\n"
    f"Greatest Decrease in Profits: {great_dec_month} (${greatest_dec})"
)

print(final_print)