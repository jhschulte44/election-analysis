# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0
# Candidate options list
candidate_options = []
# Create dictionary to count votes for candidates
candidate_votes = {}
# Winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file
with open(file_to_load) as election_data:

    # read and analyze data here
    file_reader = csv.reader(election_data)

    # read header
    headers = next(file_reader)
    
    # print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1
        # Print candidate name for each row
        candidate_name = row[2]
        # If candidate name does not match existing list
        if candidate_name not in candidate_options:
            # Add candidate name from each row
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to candidates count
        candidate_votes[candidate_name] += 1 

    # Write results into text file
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------\n")
        print(election_results, end="")
        txt_file.write(election_results)
            
# Determine percentages of votes for each candidate
# Iterate through list of candidates
for candidate_name in candidate_votes:
    # Retrieve vote count
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of total
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print out each candidates name, vote count, and percentage of total vote
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

     # Determine if vote count is greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If greater, set winning_count = votes and winning_percent = vote_percent
        winning_count = votes
        winning_percentage = vote_percentage
        # Set winning candidate to candidate's name
        winning_candidate = candidate_name
   
# Print winning candidate, vote count, and percentage
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
#print(winning_candidate_summary)
    


