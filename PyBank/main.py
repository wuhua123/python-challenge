import os
import csv
import string

# initialize needed variables
months = 0
profit_sum = 0
greatest_inc = 0
greatest_incMonth = ''
greatest_dec = 0
greatest_decMonth = ''

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header and find out all required items or value
    for row in csvreader: 
        #print(row)

        months = months + 1

        profit_sum = profit_sum + int(row[1])

        if int(greatest_inc) < int(row[1]):
            greatest_inc = int(row[1])
            greatest_incMonth = row[0]
        
        if int(greatest_dec) > int(row[1]):
            greatest_dec = int(row[1])
            greatest_decMonth = row[0]
    
    average_change = profit_sum / months
    
    #format number to USA dollar
    if average_change >= 0: 
        average_change = '${:,.2f}'.format(average_change)
    else:
        average_change = '-${:,.2f}'.format(-average_change)

    if greatest_inc >= 0:
        greatest_inc = '${:,.0f}'.format(greatest_inc) 
    else:
        greatest_inc = '-${:,.0f}'.format(-greatest_inc)

    if greatest_dec >= 0:
        greatest_dec = '${:,.0f}'.format(greatest_dec)
    else:
        greatest_dec = '-${:,.0f}'.format(-greatest_dec)
    
#Print result to terminal 
summary_dictionary = {"Total Months": months,
"Total": profit_sum,
"Average Change": average_change,
"Greatest Increase in Profits": [greatest_inc, greatest_incMonth],
"Greatest Decrease in Profits": [greatest_dec, greatest_decMonth]}

output_head_line1 = "Financial Analysis"
output_head_line2 = "----------------------------"

print()
print(output_head_line1)
print(output_head_line2)

print(f'Total Months: {summary_dictionary["Total Months"]}')
print(f'Total: {summary_dictionary["Total"]}')
print(f'Average Change: {summary_dictionary["Average Change"]}')
print("Greatest Increase in Profits: " + str(summary_dictionary["Greatest Increase in Profits"][1]) + " (" + str(summary_dictionary["Greatest Increase in Profits"][0]) +")")
print("Greatest Decrease in Profits: " + str(summary_dictionary["Greatest Decrease in Profits"][1]) + " (" + str(summary_dictionary["Greatest Decrease in Profits"][0]) +")")

# output result to txt file
# Specify the file to write to
output_path = os.path.join("output", "PyBank_output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='\n') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter='\n')

    # Write the title rows
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------------------"])

    # Write the content rows
    csvwriter.writerow(["Total Months: ", summary_dictionary["Total Months"]])
    csvwriter.writerow(["Total: ", str(summary_dictionary["Total"])])
    csvwriter.writerow(["Average Change: ", str(summary_dictionary["Average Change"])])
    csvwriter.writerow(["Greatest Increase in Profits: ", str(summary_dictionary["Greatest Increase in Profits"][1]), " (", str(summary_dictionary["Greatest Increase in Profits"][0]), ")"])
    csvwriter.writerow(["Greatest Decrease in Profits: ", str(summary_dictionary["Greatest Decrease in Profits"][1]), " (", str(summary_dictionary["Greatest Decrease in Profits"][0]), ")"])

# Get rid of the unnecessary quotes in the output txt file
with open(output_path, "r", newline='\n') as f:
    
    csvreader = csv.reader(f, delimiter='\n')
    
    for line in csvreader:
        for word in line:
            word = word.replace('\"','')