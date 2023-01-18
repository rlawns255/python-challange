import os
import csv

#reference Csv file

bank_csv = os.path.join("..", "Resources", "budget_data.csv")
#list for data
month_count=[]
profit_sum=0
average_change=0
average_sum=0
row_count=0
#Display Initial Message
print("Financial Analysis")
print("-----------------------")

#open csv and read lines subtract 1 for empty header
with open(bank_csv) as bankcsvfile:
    bankreader = csv.reader(bankcsvfile, dialect='excel', delimiter=",")
    month_count = len(bankcsvfile.readlines())-1
    print(f'Total months:  {month_count}')
    
#open csv file to sum up profit
with open(bank_csv) as bankcsvfile:
    bankreader = csv.reader(bankcsvfile, dialect='excel', delimiter=",")
    
    next(bankreader)
    
    profit_sum= sum(int(row[1]) for row in bankreader)
    print(f'Total: ${profit_sum}')

#open csv to get average change
with open(bank_csv) as bankcsvfile:
    bankreader = csv.reader(bankcsvfile, dialect='excel', delimiter=",")   
    
    next(bankreader)
    
    average_change= average_sum / month_count
    
    
print("Average Change: ")
print("Greatest Increase in profits: "+" month "+" (price) ")
print("Greatest Descrease In profits: "+" month "+" (price) " )
