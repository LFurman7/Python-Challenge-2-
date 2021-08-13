import os
import csv

# identify file path
csvpath = os.path.join(".", "Resources", "Election_data.csv")

# Open and read csv
with open(csvpath) as csv_file:
    # split by commas
    csv_reader = csv.reader(csv_file, delimiter=",")

    #skip header
    header = next(csv_reader)

    # define function and set sole parameter
def Poll_Totals(Election_data):
    #describe variables
    Voter_ID = str(Election_data[0])
    County = str(Election_data[1])
    Candidate = str(Election_data[2])

    
    Total_Votes = len(Voter_ID)













    print("The total amount of votes is: " + Total_Votes)
     ,  , UY
     U