import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from ..constants import AVG_CSV, ETHNICITY_HEATMAP

df_avg = pd.read_csv(AVG_CSV)

# Heatmap 1: rendimiento promedio
pivot_mean = df_avg.pivot_table(
    values="avg_score",
    index="race/ethnicity",
    columns="lunch",
    aggfunc="mean"
)

# Heatmap 2: cantidad de estudiantes
pivot_count = df_avg.pivot_table(
    index="race/ethnicity",
    columns="lunch",
    aggfunc="size"
)

sns.set(style="white")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Mapa de calor del rendimiento
sns.heatmap(
    pivot_mean,
    annot=True,
    fmt=".1f",
    cmap="YlOrRd",
    ax=axes[0]
)
axes[0].set_title("Rendimiento académico promedio")
axes[0].set_xlabel("Tipo de almuerzo")
axes[0].set_ylabel("Grupo étnico")

# Mapa de calor de población
sns.heatmap(
    pivot_count,
    annot=True,
    fmt="d",
    cmap="Blues",
    ax=axes[1]
)
axes[1].set_title("Cantidad de estudiantes")
axes[1].set_xlabel("Tipo de almuerzo")
axes[1].set_ylabel("")

plt.suptitle(
    "Mapas de calor por grupo étnico y tipo de almuerzo",
    fontsize=14
)

plt.tight_layout()
plt.savefig(ETHNICITY_HEATMAP, dpi=300, bbox_inches="tight")
plt.show()
