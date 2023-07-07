#create the file
import os
#Read the csv file
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))

election_csv= os.path.join('..', 'Resources', 'election_data.csv')


total_votes = 0

candidate_choices = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)



    for row in csvreader:
        total_votes = total_votes + 1
        candidates = row[2]

        if candidates not in candidate_choices:
            candidate_choices.append(candidates)

            candidate_votes[candidates] = 0 

        candidate_votes[candidates] = candidate_votes[candidates] + 1

    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) *100

        

results = (
    f"Election results\n"
    f"------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------\n"
    f"{candidate_choices}: {vote_percentage}% ({votes:,})\n"
    f"------------------\n"
    f"Winner: {winning_candidate}\n"
    f"------------------\n"
)

print(results)

output_file = os.path.join("analysis", "PyPoll_final.txt")

with open(output_file, "w", newline= '') as datafile:
    datafile.write(results)

