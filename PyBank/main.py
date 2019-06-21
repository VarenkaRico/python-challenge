import os
import csv

#Defines file in current folder
csvpath= os.path.join("HWK 03 Budget Data.csv")
finalreport=os.path.join("HWK 03 Final Report Budget Data.txt")
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',') #Reads file
    Months=-1 #Para descartar primera línea (header)
        
    for row in csvreader: #To read all the lines in the file
        Months=Months+1 #Counter of rows, which is the same as total months (1 row per month)
        if Months == 0: #If Months = 0, then is the header of the file
            Net= 0 #Sets Net in 0 to star adding
        elif Months == 1: #If 1, then first row to establish initial values
            Net = int(row[1]) #First month Profit/Loss to be added to following month-values
            G_Increase = int(row[1]) #First month Profit/Loss to be compared with following month-values
            Month_G_Inc= row[0]
            G_Decrease = int(row[1]) #First month Profit/Loss to be compared with following month-values
            Month_G_Dec = row[0]
            
        else: #If initial values are established then
            Net = Net + int(row[1]) #Sum current row value to last Net Value
            if G_Increase < int(row[1]): #Compare if current value is lower Greatest Increase
                G_Increase = int(row[1]) #If so, change Greatest Increase to current value
                Month_G_Inc = row[0] #Save Month in variable of current value
                
            else: #If not, keep values of Greatest Increase
                G_Increase = G_Increase 
                Month_G_Inc = Month_G_Inc
                
            if G_Decrease > int(row[1]): #Compare if current value is higher than Greatest Decrease
                G_Decrease = int(row[1]) #If so, change Greatest Decrease to current value
                Month_G_Dec = row[0] #Save Month in variable of current value
            else: #If not, keep values of Greatest Decrease
                G_Decrease = G_Decrease
                Month_G_Dec = Month_G_Dec

Avg_Net = int(Net) // int(Months) #Obtain average change by dividing Total Profit/Loss by Total Months. 
                                    #Double // to avoid decimals
Total_Months=str(Months)
Total_Net=str(Net)

line1="Financial Analysis"
line2="-------------------------------"
line3="Total Months: " + Total_Months
line4="Total: $" + str(Total_Net)
line5="Average Change: $" + str(Avg_Net)
line6="Greatest Increase in Profits: " + str(Month_G_Inc) + " $" + str(G_Increase)
line7="Greatest Decrease in Profits: " + str(Month_G_Dec) + " $" + str(G_Decrease)
#Print final report
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)

text_file=open(finalreport,"w") #Rewrite Final report with actual values
text_file.write(line1 + "\n" + #+ "\n" + to print in next line
    line2+ "\n" +
    line3+ "\n" +
    line4+ "\n" +
    line5+ "\n" +
    line6+ "\n" +
    line7)
