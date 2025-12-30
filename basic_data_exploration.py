import pandas as pd

data = pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\문서\\sample.csv")

print("Rows:", data.shape[0])
print("Columns:", data.shape[1])
print("Column names:")
print(data.columns)
