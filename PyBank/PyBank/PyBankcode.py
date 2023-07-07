#create the file
import os
#Read the csv file
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))
#Set the file path
budget_csv= os.path.join('.', 'Resources', 'budget_data.csv')
#Create lists
total_months = []
total_profit = []
profit_change = []

#Open the CSV 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #read the header row
    header = next(csvreader)
    #loop through
    for row in csvreader:
        #append the total month and profit lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    #grabbing the monthly change in profits    
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i +1] - total_profit[i])


#grabbing the greatest profit incerease, decrease, and corresponding month
greatest_profit_increase = max(profit_change)
greatest_profit_decrease = min(profit_change)
greatest_increase_month = total_months[profit_change.index(greatest_profit_increase)]
greatest_decrease_month = total_months[profit_change.index(greatest_profit_decrease)]

#calculating the total change and average change.
total_change = sum(profit_change)
average = round(total_change / (len(total_months)-1),2)

#Creating the statements for output ussing \n to go to the next line
output = (
    f"Financial Analysis\n"
f"----------------------\n"
f"Total Months: {len(total_months)}\n"
f"Total: ${sum(total_profit)}\n"
f"Average Change: {average}\n"
f"Greatest Increase in Profits:{greatest_increase_month}, ${greatest_profit_increase}\n"
f"Greatest Decrease in Profits:{greatest_decrease_month}, ${greatest_profit_decrease}\n")


print(output)

#Output the file
output_file = os.path.join("analysis", "PyBank_final.txt")

#Open and write the output file
with open(output_file, "w", newline= '') as datafile:
    datafile.write(output)
