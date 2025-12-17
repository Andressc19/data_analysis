import pandas as pd
import seaborn as sns
from ..constants import NORMALIZED_CSV

# Load csv
df_students = pd.read_csv(NORMALIZED_CSV)

print("MEDIA")
print(df_students[["math score", "reading score", "writing score", "average_score"]].mean().round(2))

print("MEDIANA")
print(df_students[["math score", "reading score", "writing score", "average_score"]].median().round(2))

print("MODA")
print(df_students[["math score", "reading score", "writing score", "average_score"]].mode().iloc[0])

print("DESVIACIÓN ESTANDAR")
print(df_students[ ["math score", "reading score", "writing score", "average_score"]].std().round(2))

print("VALORES MINIMO Y MAXIMO")
cols = ["math score", "reading score", "writing score", "average_score"]

for col in cols:
    print(col.upper())
    print("min", df_students[col].min())
    print("max", df_students[col].max())
    print()

sns.histplot(df_students["average_score"], bins="auto", kde=True)