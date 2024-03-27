import os
import csv
import sys

filename = 'budget_data.csv'
csvpath = os.path.join('Resources',filename)
num_Dates = 0
total_Net = 0
ave_Change = 0
greatest_Inc = 0
greatest_Dec = 0
final_val = 0
first_val = 1
first_profit = 0
initial_val = 0
inc_Profits = ""
dec_Profits = ""
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
  
    for row in csvreader:
        num_toInt = int(row[1]) #change from list to int
        total_Net = total_Net + num_toInt 
        num_Dates = num_Dates + 1 #count number of dates in list per iteration
        if(greatest_Inc > final_val - num_toInt): #compare with the greatest increase, change if greater than
            greatest_Inc = final_val - num_toInt
            inc_Profits = row[0]
        if(greatest_Dec < final_val - num_toInt): #compare with the greatest decrease, change if less than
            greatest_Dec = final_val - num_toInt
            dec_Profits = row[0]
        final_val = num_toInt

        if first_val==1:
            first_profit = int(row[1])
            first_val =0
        if num_Dates==86:
            final_val = int(row[1])

    ave_Change = (final_val - first_profit)/(num_Dates-1) #final computation for average to include all dates



    print('FINANCIAL ANALYSIS') #Print financial analysis
    print('-----------------------------------------------')
    print(f'Total Months: {num_Dates}')
    print(f'Total: {total_Net}')
    print(f'Average Change: {ave_Change}')
    print(f'Greatest Increase in Profits: {inc_Profits} {greatest_Inc}')
    print(f'Greatest Decrease in Profits: {dec_Profits} {greatest_Dec}')

    analysispath = os.path.join('Analysis','FinancialAnalysis.txt')
    with open(analysispath,'w') as textfile: #Save to text file
        
        textfile.write('FINANCIAL ANALYSIS\n')
        textfile.write('-----------------------------------------------\n')
        textfile.write(f'Total Months: {num_Dates}\n')
        textfile.write(f'Total: {total_Net}\n')
        textfile.write(f'Average Change: {ave_Change}\n')
        textfile.write(f'Greatest Increase in Profits: {inc_Profits} {greatest_Inc}\n')
        textfile.write(f'Greatest Decrease in Profits: {dec_Profits} {greatest_Dec}\n')

 

