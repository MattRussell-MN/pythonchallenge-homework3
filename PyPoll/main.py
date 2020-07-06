# import os & poll_csv
import os
import csv

file_to_load = os.path.join("Resources", "election_data.csv")
#voting_output = os.path.join("Output", "election_table.txt")

#Define Variables
total_votes = 0

candidates = {}

# Open the CSV file and read
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

# Read the header
    header = next(reader)

# For each row in spreadsheet
    for row in reader:
        
        total_votes = total_votes + 1
        
        name = row[2]

        if name not in candidates:
            candidates[name] = 1
        else:
            candidates[name] = candidates[name] + 1

#print(total_votes)

    print("Election Results")
    print("---------------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------------")

for candidate_name, vote_count in candidates.items():
    percentage = '{0:.3%}'.format((vote_count / total_votes))
    vote_count = (vote_count)
    winner = sorted(candidates.items(), reverse=False)
    
    print(f"{candidate_name}: {percentage} {(vote_count)}")


print("---------------------------------")

print("Winner: " + str(winner[1][0]))
print("--------------------------------")