# Modules
import csv

# Set filepath of csv file
csvpath = "Submission/PyBank/Resources/budget_data.csv"

# Declare variables
month_count = 0
total_profit = 0
prior_month_profit = 0
changes = []
month_changes = []

# Open csv file with the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    
    # Read the first row as header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        
        # 1) The total number of months included in the dataset
        month_count += 1
        
        # 2) The net total amount of "Profit/Losses" over the entire period
        total_profit = total_profit + int(row[1])
        
        # 3) The changes in "Profit/Losses" over the entire period, and then the average of those changes
        # IF first row, THEN last month profit equals row 1
        if (month_count == 1):
            prior_month_profit = int(row[1])
            
            # ELSE, subtract prior month profit from current month profit
        else:
            change = int(row[1]) - prior_month_profit
            changes.append(change)
            month_changes.append(row[0])
            
            # reset prior month profit
            prior_month_profit = int(row[1])

print('Total number of months : ', month_count)
print('Total profit/loss : ', total_profit)
print('Number of changes : ', len(changes))
avg_change = sum(changes) / len(changes)
print('Average of changes : ', avg_change)

# 4) The greatest increase in profits (date and amount) over the entire period
max_change = max(changes)
max_month_indx = changes.index(max_change)
max_month = month_changes[max_month_indx]
print('Maximum change : ', max_change)
print('Maximum change date : ', max_month)

# 5) The greatest decrease in profits (date and amount) over the entire period
min_change = min(changes)
min_month_indx = changes.index(min_change)
min_month = month_changes[min_month_indx]
print('Minimum change : ', min_change)
print('Minimum change date : ', min_month)

f = open("Submission/PyBank/analysis/pybank_chien.txt",'w')
print('Total number of months : ', month_count, file=f)
print('Total profit/loss : ', total_profit, file=f)
print('Number of changes : ', len(changes), file=f)
print('Average of changes : ', avg_change, file=f)
print('Maximum change : ', max_change, file=f)
print('Maximum change date : ', max_month, file=f)
print('Minimum change : ', min_change, file=f)
print('Minimum change date : ', min_month, file=f)
f.close()