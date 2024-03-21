import os
import csv
import sys

filename = 'budget_data.csv'
csvpath = os.path.join('Resources',filename)
date = {}
num_Dates = 0
total_Net = 0
ave_Change = 0
greatest_Inc = 0
greatest_Dec = 0
inc_Profits = ""
dec_Profits = ""
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
  
    for row in csvreader:
        num_toInt = int(row[1]) #change from list to int
        total_Net = total_Net + abs(num_toInt) #absolute value to compute for net losses/profit
        ave_Change = ave_Change + num_toInt #change with losses and profit
        num_Dates = num_Dates + 1 #count number of dates in list per iteration
        if(num_toInt > greatest_Inc): #compare with the greatest increase, change if greater than
            greatest_Inc = num_toInt
            inc_Profits = row[0]
        if(num_toInt < greatest_Dec): #compare with the greatest decrease, change if less than
            greatest_Dec = num_toInt
            dec_Profits = row[0]

    ave_Change = (ave_Change/num_Dates) #final computation for average to include all dates



    print('FINANCIAL ANALYSIS') #Print financial analysis
    print('-----------------------------------------------')
    print(f'Total Months: {num_Dates}')
    print(f'Total: {total_Net}')
    print(f'Average Change: {ave_Change}')
    print(f'Greatest Increase in Profits: {inc_Profits} {greatest_Inc}')
    print(f'Greatest Decrease in Profits: {dec_Profits} {greatest_Dec}')

    analysispath = os.path.join('Analysis','FinancialAnalysis.txt')
    with open(analysispath,'w') as textfile: #Save to text file
        sys.stdout = textfile
        print('FINANCIAL ANALYSIS')
        print('-----------------------------------------------')
        print(f'Total Months: {num_Dates}')
        print(f'Total: {total_Net}')
        print(f'Average Change: {ave_Change}')
        print(f'Greatest Increase in Profits: {inc_Profits} {greatest_Inc}')
        print(f'Greatest Decrease in Profits: {dec_Profits} {greatest_Dec}')

 

