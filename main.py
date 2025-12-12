import pandas as pd
from app.utils import write_dataset
from app.validations import check_column_na, check_unique, normalize_to_upper, check_range
from constants import DATA_DIR, RAW_CSV, AVG_CSV, NORMALIZED_CSV

# read csv file
df_raw = pd.read_csv(RAW_CSV)

# cleaning, checks nulls and summary in dataset
df_normalized = normalize_to_upper(df_raw)

# create a new csv file with normalized values
write_dataset(
    df_normalized,
    NORMALIZED_CSV
)

check_unique(df_normalized)
check_column_na(df_normalized)
check_range(df_normalized)

# load normalized csv file
df_normalized = pd.read_csv(NORMALIZED_CSV)

# create a new dataset file with avg score column
def getAvgScore():
    write_dataset(
        df_normalized,
        AVG_CSV,
        lambda df: df.assign(
            avg_score = df[["math score", "reading score", "writing score"]].mean(axis=1)
        )
    )

# parental level of education (PLE) vs avg_score (AVG)
def getPleAvg():
    write_dataset(
        AVG_CSV,
        f"{DATA_DIR}/StudentsPerformance_PLE_AVG.csv",
        lambda df: df.groupby("parental level of education")["avg_score"].mean().reset_index()
    )

# lunch type (LUNCH) vs avg_score (AVG) 
def getLunchAvg():
    write_dataset(
        AVG_CSV,
        f"{DATA_DIR}/StudentsPerformance_LUNCH_AVG.csv",
        lambda df: df.groupby("lunch")["avg_score"].mean().reset_index()
    )

# preparation course (TPC) vs avg_score (AVG) 
def getTpcAvg():
    write_dataset(
        AVG_CSV,
        f"{DATA_DIR}/StudentsPerformance_TPC_AVG.csv",
        lambda df: df.groupby("test preparation course")["avg_score"].mean().reset_index()
    )