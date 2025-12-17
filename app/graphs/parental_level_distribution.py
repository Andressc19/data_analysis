import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from ..constants import NORMALIZED_CSV

# Load csv
df_students = pd.read_csv(NORMALIZED_CSV)

print(df_students['parental level of education'].value_counts())
sns.set(style="whitegrid", context="talk")

plt.figure(figsize=(9, 5))

order = df_students["parental level of education"].value_counts().index

ax = sns.countplot(
    data=df_students,
    y="parental level of education",
    order=order,
    palette="pastel"
)

ax.set_title("Distribución por nivel educativo de los padres", pad=15)
ax.set_xlabel("Frecuencia")
ax.set_ylabel("Nivel educativo de los padres")


for p in ax.patches:
    ax.annotate(
        f"{int(p.get_width())}",
        (p.get_width(), p.get_y() + p.get_height() / 2),
        ha="left",
        va="center",
        fontsize=10
    )

plt.tight_layout()

# Export chart
plt.savefig("outputs/parentar_level_distribution.png", dpi=300, bbox_inches="tight")

plt.show()