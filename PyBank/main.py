import os
import csv


csvpath = os.path.join('Resources','budget_data.csv')

# Variables / Lists
change = []
dates = []
pl = []

# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader, None)


# total months
    data_set = list(csvreader)
    total_months = len(data_set)

# loop
for i in data_set:
        pl.append(int(i[1]))
        dates.append(i[0])
total = sum(pl)

# append list with loop
for j in range(1,len(pl)):
        change.append(pl[j] - pl[j-1])
        greatest_inc = max(change)
        greatest_dec = min(change)
avg_change = sum(change) / len(change)

greatestdate = str(dates[change.index(max(change)) + 1])
lowestdate = str(dates[change.index(min(change)) + 1])


# print
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total:,}')
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increase in Profits: {greatestdate} (${greatest_inc:,})')
print(f'Greatest Decrease in Profits: {lowestdate} (${greatest_dec:,})')




output_path = os.path.join('analysis', 'output.txt')

with open(output_path, 'w', newline='') as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${avg_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatestdate}, (${greatest_inc})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {lowestdate}, (${greatest_dec})\n")