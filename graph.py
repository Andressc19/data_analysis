import matplotlib.pyplot as plt
import pandas as pd
from constants import AVG_CSV
import seaborn as sns

df = pd.read_csv(AVG_CSV)

df_ms = df["math score"]
df_rs = df["reading score"]
df_ws = df["writing score"]
df_avg = df["avg_score"]

df_allmean = [df_ms.mean(), df_rs.mean(), df_ws.mean(), df_avg.mean()]

print("MEDIA MATH SCORE: \n",df_ms.mean())
print("MEDIA READING SCORE: \n",df_rs.mean())
print("MEDIA WRITING SCORE: \n",df_ws.mean())
print("MEDIA AVG SCORE:\n",df_avg.mean())

sns.histplot(df_avg, bins=30, kde=True)
plt.show()

sns.histplot(data=df, x='avg_score', hue='race/ethnicity', kde=True)
plt.show()
