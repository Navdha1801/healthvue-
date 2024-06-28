import pandas as pd

data = pd.read_csv("healthcare_dataset.csv")


data['Date of Admission'] = pd.to_datetime(data['Date of Admission'])
data['Discharge Date'] = pd.to_datetime(data['Discharge Date'])


data['Duration of Stay'] = (data['Discharge Date'] - data['Date of Admission']).dt.days.astype(int)

grouped_data = data.groupby(['Medical Condition', 'Admission Type'])['Duration of Stay'].mean().reset_index()


grouped_data['Duration of Stay'] = grouped_data['Duration of Stay'].astype(int)


grouped_data.to_csv("q2.csv", index=False)
