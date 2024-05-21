# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

# Modules
import csv
from collections import defaultdict


# Set filepath of csv file
csvpath = "Submission/PyPoll/Resources/election_data.csv"

# Declare variables
total_votes = 0
candidate_dict = {}

# Open csv file with the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    
    # Read the first row as header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        # The total number of votes cast
        total_votes += 1

        ## Add to the dictionary the following:
        # A complete list of candidates who received votes
        # The total number of votes each candidate won
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1

# The winner of the election based on popular vote
# The percentage of votes each candidate won
winner = max(candidate_dict, key=candidate_dict.get)
results = []
for candidate, vote_count in candidate_dict.items():
    percentage = (vote_count / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({vote_count})")

f = open("Submission/PyPoll/analysis/pypoll_chien.txt",'w')
print("Total number of votes cast : ", total_votes, file=f)
print("Winner by popular vote :", winner, file=f)
print("List of candidates including % and # of votes won :", results, file=f)
f.close()