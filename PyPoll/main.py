import os
import csv

# Variables
Correy_Count = 0
Khan_Count = 0
Li_Count = 0
Otooley_Count = 0
Total_Count = 0

# Set Path For File
csvpath = os.path.join('Resources', 'election_data.csv')

# Open & Read CSV File
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        
        # Find Total Number Of Votes 
        Total_Count += 1
        
        # Find Total Number Of Votes For Each Candidate
        if (row[2] == "Khan"):
            Khan_Count += 1
        elif (row[2] == "Correy"):
            Correy_Count += 1
        elif (row[2] == "Li"):
            Li_Count += 1
        else:
            Otooley_Count += 1
            
    # Find % Of Votes For Each Candidate 
    KhanPercentage = (Khan_Count / Total_Count)
    CorreyPercentage = (Correy_Count / Total_Count)
    LiPercentage = (Li_Count / Total_Count)
    OtooleyPercentage = (Otooley_Count / Total_Count)
    
    # Find Winner Based on Highest %
    winner = max(KhanPercentage, CorreyPercentage, LiPercentage, OtooleyPercentage)

    if winner == KhanPercentage:
        winner_name = "Khan"
    elif winner == CorreyPercentage:
        winner_name = "Correy"
    elif winner == LiPercentage:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {Total_Count}")
print(f"---------------------------")
print(f"Kahn: {KhanPercentage:.3%}({Khan_Count})")
print(f"Correy: {CorreyPercentage:.3%}({Correy_Count})")
print(f"Li: {LiPercentage:.3%}({Li_Count})")
print(f"O'Tooley: {OtooleyPercentage:.3%}({Otooley_Count})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

#  Set File To Write To
output_file = os.path.join('analysis', 'output.txt')
with open(output_file, 'w',) as txtfile:

# Write in Text File
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {Total_Count}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {KhanPercentage:.3%}({Khan_Count})\n")
    txtfile.write(f"Correy: {CorreyPercentage:.3%}({Correy_Count})\n")
    txtfile.write(f"Li: {LiPercentage:.3%}({Li_Count})\n")
    txtfile.write(f"O'Tooley: {OtooleyPercentage:.3%}({Otooley_Count})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")

