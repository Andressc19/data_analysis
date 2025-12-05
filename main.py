import pandas as pd

# read csv file
df = pd.read_csv("datasets/StudentsPerformance.csv")

# average score in each field
average_score = df[["math score", "reading score", "writing score"]].mean()

# relation of parental level education and avg score
df["avg_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)
df_ple_avg = df.groupby("parental level of education")["avg_score"].mean()
print(f"========== PARENTAL EDUCATION / AVG SCORE ==========\n{df_ple_avg}")

# average score per gender
df_avg_gender = df.groupby("gender")["avg_score"].mean() 
print(f"========== AVG PER GENDER ==========\n{df_avg_gender}")

# average score vs preparation course
df_avg_prc = df.groupby("test preparation course")["avg_score"].mean()
print(f"========== AVG / PREPARATION COURSE ==========\n{df_avg_prc}")