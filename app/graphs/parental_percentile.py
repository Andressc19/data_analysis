import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from ..constants import AVG_CSV, PARENTAL_PERCENTILE

df_avg = pd.read_csv(AVG_CSV)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 5))

sns.boxplot(
    data=df_avg,
    x="parental level of education",
    y="avg_score"
)

plt.title("Rendimiento académico según nivel educativo parental")
plt.xlabel("Nivel educativo parental")
plt.ylabel("Promedio de calificaciones")
plt.xticks(rotation=30, ha="right")

plt.tight_layout()
plt.savefig(PARENTAL_PERCENTILE, dpi=300, bbox_inches="tight")
plt.show()
