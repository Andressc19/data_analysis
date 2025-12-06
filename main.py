import pandas as pd

SOURCE_CSV = "datasets/StudentsPerformance.csv"
AVG_CALCULATED = "datasets/StudentsPerformance_AVG.csv"

# read csv file
df_raw = pd.read_csv(SOURCE_CSV)

# average score in each field
average_score = df_raw[["math score", "reading score", "writing score"]].mean()

# relation of parental level education and avg score
df_raw["avg_score"] = df_raw[["math score", "reading score", "writing score"]].mean(axis=1)
df_ple_avg = df_raw.groupby("parental level of education")["avg_score"].mean()

# write AVG column on csv
df_raw.to_csv(path_or_buf=AVG_CALCULATED)
df = pd.read_csv(AVG_CALCULATED)

print(f"========== PARENTAL EDUCATION / AVG SCORE ==========\n{df_ple_avg}")

# average score per gender
df_avg_gender = df.groupby("gender")["avg_score"].mean() 
print(f"========== AVG PER GENDER ==========\n{df_avg_gender}")

# average score vs preparation course
df_avg_prc = df.groupby("test preparation course")["avg_score"].mean()
print(f"========== AVG / PREPARATION COURSE ==========\n{df_avg_prc}")

# group by group 
df_group = df.groupby("race/ethnicity").size()
print(f"========== COUNT / GROUP ==========\n{df_group}")
