import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ..constants import NORMALIZED_CSV, ETHNICITY_DISTRIBUTION

# Load csv
df_students = pd.read_csv(NORMALIZED_CSV)

print(df_students['race/ethnicity'].value_counts())
sns.set(style="whitegrid", context="talk")

plt.figure(figsize=(9, 5))

# Ordenar por frecuencia
order = df_students["race/ethnicity"].value_counts().index

ax = sns.countplot(
    data=df_students,
    x="race/ethnicity",
    order=order,
    palette="pastel"
)

# Títulos y etiquetas
ax.set_title("Distribución por raza/etnia", pad=15)
ax.set_xlabel("Grupo racial/étnico")
ax.set_ylabel("Frecuencia")


for p in ax.patches:
    ax.annotate(
        f"{int(p.get_height())}",
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()

# Export chart
plt.savefig(ETHNICITY_DISTRIBUTION, dpi=300, bbox_inches="tight")

plt.show()