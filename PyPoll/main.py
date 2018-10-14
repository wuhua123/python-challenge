import os
import csv

# define variables
Total_CastNum = 0

# direct file path
csv_path = os.path.join('Resources', 'election_data.csv')

# open file with csv reader and assign content to variable
with open (csv_path, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_head = next(csvreader)

    #initialize necessary variables
    candidate_list = []
    candidate_winNum = []
    candidate_winPercent = []
    Total_CastNum = 0
    
    # loop dataset to calculate Total Cast number and place candidates and vote numbers to lists
    for row in csvreader:

        Total_CastNum += 1

        if row[2] not in  candidate_list:
            candidate_list.append(row[2])
            candidate_winNum.append(int("1"))
        else:
            index = candidate_list.index(row[2])
            candidate_winNum[index] =  candidate_winNum[index] + 1
    
    
    # Print the title rows
    print()
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: " + f'{Total_CastNum}')
    print("-----------------------------")

    # calculate vote percentage each candidate gain, find the winner and print items to screen
    winner_VoteNum = 0
    winner = ""
    i = 0
    for candidate in candidate_list:
        #index = candidate_list.index(candidate)
        candidate_winPercent.append(float(0.00000))
        candidate_winPercent[i] = int(candidate_winNum[i]) / int(Total_CastNum)
        if winner_VoteNum < candidate_winNum[i]:
            winner_VoteNum = candidate_winNum[i]
            winner = candidate
        print(candidate +":"+ str(format(candidate_winPercent[i], "10.3%")) + " (" + str(candidate_winNum[i]) + ")")
        i=i+1
    
    print("------------------------------")
    print("Winner: "+str(winner))
    print("------------------------------")

# output result to txt file
output_path = os.path.join('output', 'PyPoll_Output.txt')

with open(output_path, 'w', newline='\n') as output:

    csvwriter = csv.writer(output, delimiter='\n')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------------"])
    csvwriter.writerow(["Total Votes: ", Total_CastNum])
    csvwriter.writerow(["-----------------------------"])
    
    i = 0
    for candidate in candidate_list:
        csvwriter.writerow([candidate,":", str(format(candidate_winPercent[i], "10.3%")), " (", str(candidate_winNum[i]), ")"])
        i=i+1
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow(["Winner: ", str(winner)])
    csvwriter.writerow(["------------------------------"])




    


        


