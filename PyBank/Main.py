import os
import csv


csvpath = os.path.join("Resources" , "Budget_data.csv")

prof_loss = []
months = []

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    print(f"Header: {csv_header}")
    for row in csv_reader: 
        prof_loss.append(row[1])
        months.append(row[0])

total_months = (len(months))

net_total = sum(prof_loss)

avg_changes = net_total / total_months

minimum_prof = min(prof_loss)
maximum_prof = max(prof_loss)

max_index = prof_loss.index(maximum_prof)
min_index = prof_loss.index(minimum_prof)

max_months = months[max_index]
min_months = months[min_index]

output_path = os.path.join("analysis", "PyBank_Analysis.txt")

Output = (
    f"Financial Analysis\n"
    f" ----------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total:.2f}\n" 
    f"Average Change: {avg_changes:.2f}\n"
    f"Greatest Increase in Profits: {max_months} {maximum_prof:.2f}\n"
    f"Greatest Decrease in Profits: {min_months} {minimum_prof:.2f}\n")

print(Output)

with open('output_path', 'w') as txt_file:
    txt_file.write(Output)
