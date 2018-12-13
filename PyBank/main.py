#JLT HW3 PyBank
#fix greatest Inc/Dec month, typo on line 49 makes it work for Inc month
#format line 65 to dollars not working "${:0,.2f}"

#imports
import os
import csv

#relative path
budget_data = os.path.join("..","Resources", "budget_data.csv")

#open file and read using csv import
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    #set variables and lists
    totalMonths = 0
    totalpl = 0
    previouspl = 0
    change = []
    greatestInc = 0
    greatestDec = 0 
    #teacher had firstrow = next(csvreader) which gave ['Jan-2010', '867884']

    for row in csvreader:
        #totalMonths = len(list(csvreader))+1
        #print(totalMonths)

        #set variables
        month = row[0]
        greatestIncmnth = row[0]
        greatestDecmnth = row[0]

        #total months
        totalMonths = totalMonths + 1
        totalpl = int(row[1]) + totalpl

        #change in pl
        plchange = int(row[1]) - previouspl
        change.append(plchange)

        #identify greatest Inc/Dec
        if plchange < greatestInc:
            greatestInc = greatestInc
            greatestIncmnth = greatestIncmnth
        else: 
            greatestInc = plchange 
            greatIncmnth = month

        if plchange < greatestDec:
            greatestDec = plchange
            greatestDecmnth = month
        else: 
            greatestDec = greatestDec
            greatestDecmnth = greatestDecmnth

        #reset value
        previouspl = int(row[1])

    #strip first value from list
    change = change[1:]

    #cal avg
    plavg = sum(change)/len(change)

#prints to chk wk
# print(totalpl)
# print(totalMonths)
# print(change)
# print(plavg)
# print(greatestInc)
# print(greatestDec)
print(greatestIncmnth)
print(greatestDecmnth) 

#output
print(f"Financial Analysis")
print(f"----------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalpl}")
print(f"Average Change: {plavg}")
print(f"Greatest Increase in Profits: {greatIncmnth} (${greatestInc})")
print(f"Greatest Decrease in Profits: {greatestDecmnth} (${greatestDec})")

#put output in list
bankfiles = [["----------"],[f"Total Months: {totalMonths}"], [f"Total: ${totalpl}"], [f"Average Change: {plavg}"], [f"Greatest Increase in Profits: {greatestIncmnth} (${greatestInc})"], [f"Greatest Decrease in Profits: {greatestDecmnth} (${greatestDec})"]]

# save the file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])

    writer.writerows(bankfiles)
