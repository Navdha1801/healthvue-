import pandas as pd

df = pd.read_csv("healthcare_dataset.csv")

df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])


df['Duration of Stay'] = (df['Discharge Date'] - df['Date of Admission']).dt.days


unique_combinations = df.groupby(['Medication', 'Insurance Provider', 'Duration of Stay']).agg({'Billing Amount': 'mean'}).reset_index()


unique_combinations.to_csv("q3.csv", index=False)


print("Data has been saved to healthcare.csv")
