import pandas as pd
data = pd.DataFrame({
    'Name': ['Geek1', 'Geek2', 'Geek3', 'Geek4', 'Geek5'],
    'Age': [25, 30, 22, 35, 28],
    'Salary': [50000, 60000, 45000, 70000, 55000]
})
data.set_index('Name', inplace=True)
print("Original DataFrame:")
print(data)
row_alice = data.iloc[0, :]
print("\nExtracted Row (Geek1):")
print(row_alice)
rows_geek2_to_geek3 = data.iloc[1:3, :]
print("\nExtracted Rows (Geek2 to Geek3):")
print(rows_geek2_to_geek3)
