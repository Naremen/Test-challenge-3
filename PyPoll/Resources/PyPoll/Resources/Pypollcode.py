#create the file
import os
#Read the csv file
import csv

#loading in the path to code
os.chdir(os.path.dirname(os.path.realpath(__file__)))

election_csv= os.path.join('..', 'Resources', 'election_data.csv')

#couter for the vote
total_votes = 0
#setting lists and dicitonaries
candidate_choices = []
candidate_votes = {}
#treacks the winning candidate and count
winning_candidate = ""
winning_count = 0

#read in the csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)


    #looping throuhg each row and adding the vote count
    for row in csvreader:
        total_votes = total_votes + 1
        candidates = row[2]
        #add the list of candidates 
        if candidates not in candidate_choices:
            candidate_choices.append(candidates)
            #start tracking the votes the candidate gets
            candidate_votes[candidates] = 0 

        candidate_votes[candidates] = candidate_votes[candidates] + 1

    for candidate in candidate_votes:
        #grab the vote count and percentage.
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) *100


        
#output for the results
results = (
    f"Election results\n"
    f"------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------\n"
    f"{candidate}: {vote_percentage}% ({votes})\n"
    f"------------------\n"
    f"Winner: {winning_candidate}\n"
    f"------------------\n"
)

print(results)
#output the file
output_file = os.path.join("analysis", "PyPoll_final.txt")
#open and write the file
with open(output_file, "w", newline= '') as datafile:
    datafile.write(results)

