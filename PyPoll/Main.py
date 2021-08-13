import os
import csv

# identify file path
election = os.path.join("Resources", "Election_data.csv")

count = {}
total = 0
percent = {}
winner = 0


with open(election) as csv_file:
    elect_reader = csv.reader(csv_file, delimiter=",")

    header = next(elect_reader)

    for row in elect_reader:
        total += 1
        if row[2] in count:
            count[row[2]] += 1

        else:
            count[row[2]] = 1

for candidate in count:
    percent[candidate] = (count[candidate] / total) * 100

    if count[candidate] > winner:
        winner= count[candidate]
        won = candidate

output_path = os.path.join('Analysis', 'Election_Analysis.txt')

with open(output_path, 'w', newline="") as txtfile:

    txtfile.write(f'''
        Election Results
        -------------------------
        Total Votes: {total}
        -------------------------\n''')

    print(f'''\nElection Results
        -------------------------
        Total Votes: {total}
        -------------------------''')

    for candidate, votes in count.items():
        txtfile.write(f'{candidate}: {percent[candidate]:.3f}% ({votes})\n')
        
        print(f'''{candidate}: {percent[candidate]:.3f}% ({votes})''')
    
        txtfile.write(f'''-------------------------
            Winner: {won}
            -------------------------''')

        print(f'''-------------------------
         Winner: {won}
            -------------------------''')


