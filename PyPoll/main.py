# import dependencies
import csv
# used to export script
import sys

# csv path
csv_path = "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"

# variable for total votes set to 0
total_votes = 0

candidate_options = []
candidate_votes = {}

# variables to track winning candidate and amount of votes
winning_candidate = ""
winning_count = 0

# open and read csv and convert it into a list of dictionaries
with open(csv_path) as election_data:
    reader = csv.DictReader(election_data)
    # exports to txt file
    sys.stdout = open('final_results.txt', 'w')

    for row in reader:

        # calculates total votes
        total_votes = total_votes + 1

        # pulls the candidate names from rows
        candidate_name = row["Candidate"]

        # finding candidate names
        if candidate_name not in candidate_options:

            # adds candidate names to the list
            candidate_options.append(candidate_name)

            # tracks the candidate's voter count
            candidate_votes[candidate_name] = 0

        # adds a vote to the candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    # prints the final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results)

    for candidate in candidate_votes:

        # finds the vote count for each candidate and calculates the percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # finds the winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # prints each candidate's vote count and percentage
        voter_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_results)

    # prints the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)