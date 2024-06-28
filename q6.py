import csv
from collections import Counter


with open('healthcare_dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)


condition_bloodtype_counter = Counter()


for row in data:
    medical_condition = row['Medical Condition']
    blood_type = row['Blood Type']
    condition_bloodtype_counter[(medical_condition, blood_type)] += 1


with open('q7.csv', 'w', newline='') as file:
    fieldnames = ['Medical Condition', 'Blood Type', 'Number of Individuals']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

  
    for (condition, blood_type), count in condition_bloodtype_counter.items():
        writer.writerow({'Medical Condition': condition, 'Blood Type': blood_type, 'Number of Individuals': count})