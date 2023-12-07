# Import Modules
import os, csv
from pathlib import Path 

# Path to collect data from the Resources folder
election_csv = Path("Resources", "election_data.csv")

# Declare Variables 
charles_votes = 0 
diana_votes = 0
raymon_votes = 0
total_votes = 0 


# Read in the CSV file
with open(election_csv) as elections:

    # Split the data on commas
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header 
    header = next(csvreader)     

    #  Loop through the data
    for row in csvreader: 

        # Count total_votes
        total_votes +=1

        #Count votes for each candidate
        if row[2] == "Charles Casper Stockham": 
            charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            raymon_votes +=1

 #Create a dictionary out of the lists previously created 
candidates_name = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes_list = [charles_votes, diana_votes,raymon_votes]

# Zip the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates_name,votes_list))
winner = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# A summary for each candidate
charles_percent = (charles_votes/total_votes) *100
diana_percent = (diana_votes/total_votes) * 100
raymon_percent = (raymon_votes/total_votes)* 100


# Print ot a Summary table

print("\n")
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")
print("\n")
# Output files

output_file = Path("Analysis", "Election_Summary.txt")

with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")