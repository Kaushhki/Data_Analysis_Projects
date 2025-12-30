import pandas as pd
data = pd.read_csv("C:\\Users\\Lenovo\\Downloads\\archive\\STUDENT_DATASET.csv")  


print("Rows:", data.shape[0])
print("Columns:", data.shape[1])
print("Column names:")
print(data.columns)


print("\nAverage marks:", data["Marks"].mean())
print("Highest marks:", data["Marks"].max())
print("Lowest marks:", data["Marks"].min())


if "percentage" in data.columns:
    print("Average percentage:", data["percentage"].mean())

import matplotlib.pyplot as plt

plt.bar(data["name"], data["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")
plt.show()
