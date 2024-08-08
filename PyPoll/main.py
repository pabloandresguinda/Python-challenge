
# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote


import os
import csv
from pprint import pprint

# Set path for file
csvdata = os.path.join("PyPoll","Resources", "election_data.csv")

# Open the CSV using the UTF-8 encoding
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
with open(csvpath, 'r') as csvfile:
    poll_csv = csv.reader(csvfile, delimiter=',')
    csv_header = next(poll_csv)
    data = [item for item in poll_csv]

# The total number of votes 

total_votes = len(data)

print ("Election Results")
print ("-"*30)


# Set of unique candidates
candidates_set = set()

for row in data:
    # Add the candidate name to the set
    candidates_set.add(row[2])

candidate_list = sorted(candidates_set)

# Find the candidate votes

# Calculate the number of votes for each candidate 
votes_per_candidate = {}

for row in data:
    candidate = row[2]
    if candidate in votes_per_candidate:
        votes_per_candidate[candidate] += 1
    else:
        votes_per_candidate[candidate] = 1

# Step 3: Calculate the percentage of votes each candidate won
percentage_per_candidate = {}

for candidate, votes in votes_per_candidate.items():
    percentage_per_candidate[candidate] = (votes / total_votes) * 100

# Step 4: Determine the winner based on popular vote
winner = max(votes_per_candidate, key=votes_per_candidate.get)

# Print the results
print(f"Total Votes: {total_votes}")
print ("-"*30)
for candidate in votes_per_candidate:
    print(f"{candidate}: {votes_per_candidate[candidate]} votes, {percentage_per_candidate[candidate]:.2f}%")
print ("-"*30)
print(f"Winner: {winner}")
print ("-"*30)

# Exporting to .txt file
to_file = (
    f"Election Results\n"
    f"------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------------\n")

for x in votes_per_candidate:
    to_file += (f"{candidate}: {votes_per_candidate[x]} votes, "
                f"{percentage_per_candidate[x]:.2f}%\n")

to_file += f"Winner: {winner}\n"

textpath = os.path.join('PyPoll', 'analysis', 'results.txt')
with open(textpath, 'w') as resultsfile:
    resultsfile.write(to_file)



