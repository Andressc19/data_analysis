import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ..constants import NORMALIZED_CSV, COURSE_DISTRIBUTION_GRAPH

# Load csv
df_students = pd.read_csv(NORMALIZED_CSV)

print(df_students['test preparation course'].value_counts())
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid", context="talk")

plt.figure(figsize=(7, 5))

order = df_students["test preparation course"].value_counts().index

palette = {
    "COMPLETED": "#5DA9A4",
    "NONE": "#B0B0B0" 
}

ax = sns.countplot(
    data=df_students,
    x="test preparation course",
    order=order,
    palette=palette
)

ax.set_title("Distribución por curso de preparación para el examen", pad=15)
ax.set_xlabel("Curso de preparación")
ax.set_ylabel("Frecuencia")

# Valores encima de las barras
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
plt.savefig(COURSE_DISTRIBUTION_GRAPH, dpi=300, bbox_inches="tight")

plt.show()