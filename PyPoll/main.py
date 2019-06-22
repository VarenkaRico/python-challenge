import os
import csv

#Defines file in current folder
csvpath= os.path.join("HWK 03 Election Data.csv")
finalresults=os.path.join("HWK 03 Final Report Election Data.txt")
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',') #Reads file

    Candidates=[]
    Votes=[]
    Voters=-1
    percentage_Votes=[]
    for row in csvreader:
        if Voters == -1:
            Candidates=[]
            Voters=0
        else:
            Voters=Voters+1
            if row[2] in Candidates:
                Candidates=Candidates
            else:
                Candidates.append(row[2])


##Reset reading of file
for name in Candidates:
    Cand_Votes=0
    with open(csvpath,newline='') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',') #Reads file    
        for row in csvreader:
            if row[2]==name:
                Cand_Votes=Cand_Votes+1
        Votes.append(Cand_Votes)

line1="Election Results"
line2="---------------------------"
line3="Total Voters: " + str(Voters)

print(line1)
print(line2)
print(line3)
print(line2)

text_file=open(finalresults, "w+") #Rewrite Final report with actual values
text_file.write(line1 + "\n" + #+ "\n" + to print in next line
    line2+ "\n" +
    line3+ "\n" +
    line2+ "\n")
text_file.close

counter=0
VotesWinner=0

for name in Candidates:
    currentline=name + ": " +  str(round(Votes[counter]/Voters*100,5))+"% (" + str(Votes[counter]) + " votes)"
    print(currentline)
    text_file=open(finalresults,"a")
    text_file.write(currentline+ "\n")
    text_file.close
    if Votes[counter]>VotesWinner:
        VotesWinner=Votes[counter]
        Winner=name
    counter=counter+1

print(line2)
print("Winner: "+Winner)
print(line2)

text_file=open(finalresults,"a")
text_file.write(line2+ "\n" + "Winner: "+ Winner + "\n" + line2)
