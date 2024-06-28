import pandas as pd


data = pd.read_csv("healthcare_dataset.csv")


data['Date of Admission'] = pd.to_datetime(data['Date of Admission'])
data['Discharge Date'] = pd.to_datetime(data['Discharge Date'])


data['Duration'] = (data['Discharge Date'] - data['Date of Admission']).dt.days 


result = data.groupby(['Medical Condition', 'Medication'])['Duration'].mean().reset_index()
print(result)

result_json = result.to_json(orient='records')

with open('changed.json', 'w') as json_file:
    json_file.write(result_json)