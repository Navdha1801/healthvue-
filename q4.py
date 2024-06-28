import csv
from datetime import datetime

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"

def extract_fields(input_file, output_file):
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)
        fieldnames = ['Condition', 'Season']
        
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in reader:
                medical_condition = row['Medical Condition']
                admission_date = datetime.strptime(row['Date of Admission'], '%Y-%m-%d')
                season_of_admission = get_season(admission_date.month)
                
                writer.writerow({
                    'Condition': medical_condition,
                    'Season': season_of_admission
                })


input_file = 'healthcare_dataset.csv'  
output_file = 'q4.csv'  
extract_fields(input_file, output_file)

with open('q4.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)


header = data[0]
rows = data[1:]


rows.sort(key=lambda x: x[1])


with open('q4.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header) 
    writer.writerows(rows)  

print("Data sorted and written back to 'input.csv'")
