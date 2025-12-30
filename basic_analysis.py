import pandas as pd

data = pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\문서\\sample.csv")

print("Average marks:", data["marks"].mean())
print("Highest marks:", data["marks"].max())
print("Lowest marks:", data["marks"].min())
