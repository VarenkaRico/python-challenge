import os
import csv

#Defines file in current folder
csvpath= os.path.join("HWK 03 Election Data.csv")
finalresults=os.path.join("HWK 03 Final Report Election Data.txt")
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',') #Reads file

    Candidates=[] #Will list all the candidates in the file
    Votes=[] #Will list the total votes for each candidate according to the position in Candidates (first number will correspond to the votes given 
               #to first candidate in Candidates List, second number to the votes given to the second Candidats List...)
    Voters=-1 #To avoid header
    percentage_Votes=[]
    for row in csvreader: #Read each line of the csv file
        if Voters == -1: #Voters=-1, it is on the header
            Candidates=[]
            Voters=0
        else:
            Voters=Voters+1 #Counts total voters
            if row[2] in Candidates: #Determines if the Candidate has already being added to the list of Candidates
                Candidates=Candidates #If the Candidate in the row is in the List of Candidates, then it does not make changes in the list
            else:
                Candidates.append(row[2]) #If it is not in the List, then it adds him/her


##Reset reading of file
for name in Candidates: #For all the name in the list Candidates
    Cand_Votes=0
    with open(csvpath,newline='') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',') #Restart reading of the file  
        for row in csvreader: 
            if row[2]==name: #If the Candidate in the row matches the actual name in Candidate, then it adds +1 vote
                Cand_Votes=Cand_Votes+1
        Votes.append(Cand_Votes) #When it finishes reading the file, it apends the total votes of the candidate to the list Cand_Votes

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
text_file.close #Closes file

counter=0
VotesWinner=0

for name in Candidates: #Prints the information for each candidate in Candidate List + the Total Votes registered for each
    currentline=name + ": " +  str(round(Votes[counter]/Voters*100,5))+"% (" + str(Votes[counter]) + " votes)"
    print(currentline)
    text_file=open(finalresults,"a") 
    text_file.write(currentline+ "\n") #Opens text file and prints the line in the file, without earasing the past lines printed
    text_file.close
    if Votes[counter]>VotesWinner: 
        VotesWinner=Votes[counter]#defines if the current name in Candidates has more votes than the last one, 
        Winner=name #if so, is set as winner until another has more votes
    counter=counter+1 #Next value in Votes

print(line2)
print("Winner: "+Winner)
print(line2)

text_file=open(finalresults,"a")
text_file.write(line2+ "\n" + "Winner: "+ Winner + "\n" + line2)#Prints the information of the Winner in file
