# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize total vote counter
total_votes = 0

# Open election results and read file
with open(file_to_load) as election_data:

    # to-do: read and analyze data here
    file_reader = csv.reader(election_data)

    # read and print header
    headers = next(file_reader)
    
    # print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count
        total_votes += 1

# 3. Print the total votes
print(total_votes)

with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\nArapahoe\nDenver\nJefferson")



# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote