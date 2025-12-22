import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from ..constants import AVG_CSV, ETHNICITY_PERCENTILE

df_avg = pd.read_csv(AVG_CSV)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 5))

sns.boxplot(
    data=df_avg,
    x="race/ethnicity",
    y="avg_score",
    hue="lunch"
)

plt.title("Rendimiento académico por grupo étnico y tipo de almuerzo")
plt.xlabel("Grupo étnico")
plt.ylabel("Rendimiento académico promedio")
plt.legend(title="Tipo de almuerzo")

plt.tight_layout()

plt.savefig(ETHNICITY_PERCENTILE, dpi=300, bbox_inches="tight")

plt.show()