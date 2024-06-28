import csv

input_file = open('healthcare_dataset.csv', 'r')
reader = csv.DictReader(input_file)


medication_counts = {}


for row in reader:
    condition = row['Medication']
    admission_date = row['Date of Admission']
    month = admission_date.split('-')[1]

    
    if (condition, month) in medication_counts:
      
        medication_counts[(condition, month)] += 1
    else:
     
        medication_counts[(condition, month)] = 1


input_file.close()


sorted_medication_counts = sorted(medication_counts.items(), key=lambda x: x[0])


output_file = open('q4.csv', 'w', newline='')
fieldnames = ['Medication', 'Month', 'Count']
writer = csv.DictWriter(output_file, fieldnames=fieldnames)
writer.writeheader()


for (condition, month), count in sorted_medication_counts:
    writer.writerow({'Medication': condition, 'Month': month, 'Count': count})


output_file.close()