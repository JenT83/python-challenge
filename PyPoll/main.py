#JLT HW3 PyPoll
#fix cancidate counter

#imports
import os
import csv

#relative path
polldata = os.path.join("..","Resources", "election_data.csv")

#set variables 
votesK = 0
votesC = 0
votesL = 0
votesO = 0

#open file and read using csv import
with open(polldata, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)

    for row in csvreader:

        totalvotes = len(list(csvreader))+1
        #print(totalvotes)

        #total votes per candiate using loop
        if row[2] == "Khan":
            votesK = votesK + 1
        else:
            votesK = votesK
        if row[2] == "Correy":
            votesC = votesC + 1
        else:
            votesC = votesC
        if row[2] == "Li":
            votesL = votesL + 1
        else:
            votesL = votesL
        if row[2] == "O'Tooley":
            otesO = votesO + 1
        else:
            votesO = votesO

print(f'votesK {votesK}')
print(f'votesC {votesC}')
print(f'votesL {votesL}')
print(f'votesO {votesO}')

#variable for candidate votes / totalvotes. 
voteKpercent = "%.3f%%" % (100 * (votesK / totalvotes))
voteCpercent = "%.3f%%" % (100 * (votesC / totalvotes))
voteLpercent = "%.3f%%" % (100 * (votesL / totalvotes))
voteOpercent = "%.3f%%" % (100 * (votesO / totalvotes))

#determine winner
if votesK > votesC and votesK > votesL and votesK > votesO:
    winner = "Khan"
elif votesC > votesK and votesC > votesL and votesC > votesO:
    winner = "Correy"
elif votesL > votesK and votesL > votesC and votesL > votesO:
    winner = "Li"
elif votesO > votesK and votesO > votesC and votesO > votesL:
    winner = "O'Tooley"

print(winner)

#would I be able to use a print statement to run through all candidates?
print(f"Election Results")
print(f"----------")
print(f"Total Votes: {totalvotes}")
print(f"----------")
print(f"Khan: {voteKpercent} ({votesK})")
print(f"Correy: {voteCpercent} ({votesC})")
print(f"Li: {voteLpercent} ({votesL})")
print(f"O'Tooley: {voteOpercent} ({votesO})")
print(f"----------")
print(f"Winner: {winner}")
print(f"----------")

#put output in list
pollfiles = [["----------"],[f"Total Votes: {totalvotes}"], ["----------"], [f"Khan: {voteKpercent} ({votesK})"], [f"Correy: {voteCpercent} ({votesC})"], [f"Li: {voteLpercent} ({votesL})"], [f"O'Tooley: {voteOpercent} ({votesO})"], ["----------"], [f"Winner: {winner}"], ["----------"]]

# save the file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])

    writer.writerows(pollfiles)


#delete after fix candidate count in loop
#didn't save previous attempts 

    #    #Attempt3
    #     if row[2] == "Khan":
    #         votesK = votesK + 1
    #     elif row[2] == "Correy":
    #         votesC = votesC + 1
    #     elif row[2] == "Li":
    #         votesL = votesL + 1
    #     else:
    #         votesO = votesO + 1
       
    #    #Attempt4
    #    if row[2] == "Khan":
    #         votesK = votesK + 1
    #         votesC = votesC
    #         votesL = votesL
    #         votesO = votesO
    #     elif row[2] == "Correy":
    #         votesC = votesC + 1
    #         votesK = votesK
    #         votesL = votesL
    #         votesO = votesO
    #     elif row[2] == "Li":
    #         votesL = votesL + 1
    #         votesK = votesK
    #         votesC = votesC
    #         votesO = votesO
    #     else:
    #         votesO = votesO + 1
    #         votesK = votesK
    #         votesC = votesC
    #         votesL = votesL
       
    #    #Attempt5
    #    if row[2] == "Khan":
    #         votesK = votesK + 1
    #     else:
    #         votesK = votesK
    #     if row[2] == "Correy":
    #         votesC = votesC + 1
    #     else:
    #         votesC = votesC
    #     if row[2] == "Li":
    #         votesL = votesL + 1
    #     else:
    #         votesL = votesL
    #     if row[2] == "O'Tooley":
    #         otesO = votesO + 1
    #     else:
    #         votesO = votesO