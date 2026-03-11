#import pandas library
import pandas as pd

# 1. Load the file students.csv and make sure Score Date is parsed as datetime.
df = pd.read_csv("students.csv", parse_dates=["Score Date"])
print(df.head())

#2 Print the shape, columns list, and data types of the DataFrame.
print("Shape:", df.shape)

print("Columns:")
print(df.columns)

print("Data Types:")
print(df.dtypes)

