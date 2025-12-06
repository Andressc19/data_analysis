import pandas as pd

SOURCE_CSV = "datasets/StudentsPerformance.csv"

# read the csv 
df = pd.read_csv(SOURCE_CSV)

# print the null data form column
print("Datos nulos por columna")
print(df.isnull().sum())

# unique values for each column
for col in df.columns:
    print(f"\n Values únicos en '{col}':")
    print(df[col].unique())