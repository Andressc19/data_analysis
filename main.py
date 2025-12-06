import pandas as pd
from app.utils import write_dataset
from pandas import DataFrame


# define constants to src files
ROOT_DIR = "datasets"
RAW_CSV = f"{ROOT_DIR}/StudentsPerformance.csv"
AVG_CSV = f"{ROOT_DIR}/StudentsPerformance_AVG.csv"


# read csv file
df_raw = pd.read_csv(RAW_CSV)

# create a new dataset file with avg score column
write_dataset(
    RAW_CSV,
    AVG_CSV,
    lambda df: df.assign(
        avg_score = df[["math score", "reading score", "writing score"]].mean(axis=1)
    )
)

# parental level of education (PLE) vs avg_score (AVG)
write_dataset(
    AVG_CSV,
    f"{ROOT_DIR}/StudentsPerformance_PLE_AVG.csv",
    lambda df: df.groupby("parental level of education")["avg_score"].mean().reset_index()
)

# lunch type (LUNCH) vs avg_score (AVG) 
write_dataset(
    AVG_CSV,
    f"{ROOT_DIR}/StudentsPerformance_LUNCH_AVG.csv",
    lambda df: df.groupby("lunch")["avg_score"].mean().reset_index()
)

# preparation course (TPC) vs avg_score (AVG) 
write_dataset(
    AVG_CSV,
    f"{ROOT_DIR}/StudentsPerformance_TPC_AVG.csv",
    lambda df: df.groupby("test preparation course")["avg_score"].mean().reset_index()
)
