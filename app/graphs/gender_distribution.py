import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ..constants import NORMALIZED_CSV

# Load csv
df_students = pd.read_csv(NORMALIZED_CSV)

print(df_students['gender'].value_counts())

# Styles
sns.set(style="whitegrid", context="talk")

plt.figure(figsize=(8, 5))

# Palette
palette = {
    "FEMALE": "#f99aaa",
    "MALE": "#84b6f4"
}

ax = sns.countplot(
    data=df_students,
    x="gender",
    order=["FEMALE", "MALE"],
    palette=palette
)

# Titles and labels
ax.set_title("Distribución por género", pad=15)
ax.set_xlabel("Género")
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
plt.savefig("outputs/gender_distribution.png", dpi=300, bbox_inches="tight")

plt.show()