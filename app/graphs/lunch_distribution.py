import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from ..constants import NORMALIZED_CSV, LUNCH_DISTRIBUTION

# Load csv
df_students = pd.read_csv(NORMALIZED_CSV)

print(df_students['lunch'].value_counts())
sns.set(style="whitegrid", context="talk")

plt.figure(figsize=(7, 5))

order = df_students["lunch"].value_counts().index

palette = {
    "STANDARD": "#7BC47F",
    "FREE/REDUCED": "#F4A261"
}

ax = sns.countplot(
    data=df_students,
    x="lunch",
    order=order,
    palette=palette
)

ax.set_title("Distribución por tipo de almuerzo", pad=15)
ax.set_xlabel("Tipo de almuerzo")
ax.set_ylabel("Frecuencia")


for p in ax.patches:
    ax.annotate(
        f"{int(p.get_height())}",
        (p.get_x() + p.get_width() / 2, p.get_height()),
        ha="center",
        va="bottom",
        fontsize=11
    )

plt.tight_layout()

# Export chart
plt.savefig(LUNCH_DISTRIBUTION, dpi=300, bbox_inches="tight")

plt.show()