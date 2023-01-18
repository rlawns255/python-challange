import os
import csv

#reference Csv file

election_csv = os.path.join("..", "Resources", "election_data.csv")
#list for data
vote_count=[]

#Display Initial Message
print("Election Results")
print("-----------------------")

#open csv and read lines subtract 1 for empty header
with open(election_csv) as electioncsvfile:
    electionreader = csv.reader(electioncsvfile, dialect='excel', delimiter=",")
    vote_count = len(electioncsvfile.readlines())-1
    print(f'Total votes :  {vote_count}')
    

print("-----------------------")
print("Charles Casper Stockham: ")
print("Diana Degette: ")
print("Raymon Anthony Doane: " )
print("-----------------------")
print("Winner: ")
print("-----------------------")
