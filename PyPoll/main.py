
import os
import csv
import sys


csvpath = os.path.join('Resources', 'election_data.csv')




with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    election = {} #Initialize dictionary
        
        
    for row in csvreader: # Loop through file, find candidates and count votes
        election[row[2]] = election.get(row[2], 0) + 1 # while using get() method to help with first time occurance of keys, credits to https://github.com/zunicd/Vote-Counting/blob/master/main.py
    total_votes = sum(election.values()) # Calculate total number of votes
    winner, _ = max(election.items(), key = lambda k: k[1])   # Find winner --> candidate with max votes
        # k[1] is dictionary value, that is equal to count of votes, credits to https://github.com/zunicd/Vote-Counting/blob/master/main.py for this
    result = "" # Variable for keeping votes results for all candidates
    for name in election.keys():
        percent_votes = (election[name] / total_votes) * 100 # Calculate percent of votes for each candidate and place
        result = result + f"{name}: {percent_votes:.3f}% ({election[name]})\n"

  

    print("Election Results")   # Output election results
    print("-----------------------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------------------------")
    print(result)
    print("-----------------------------------------------")
    print(f"Winner: {winner}")

    analysispath = os.path.join('Analysis','ElectionResults.txt')
    with open(analysispath, 'w') as textfile: # Export election results to text file
         sys.stdout = textfile
         print("Election Results")
         print("-----------------------------------------------")
         print(f"Total Votes: {total_votes}")
         print("-----------------------------------------------")
         print(result)
         print("-----------------------------------------------")
         print(f"Winner: {winner}")
