import pandas as pd


def check_column_na(source: str):
    """
        function to check null values per column
    """
    df = pd.read_csv(source)
    print(f"Datos nulos por columna\n{df.isnull().sum()}\n")


def check_unique(source: str):
    """
        function to check unique values for each column
    """
    df = pd.read_csv(source)
    for col in df.columns:
        print(f"Valores únicos en la columna '{col}':\n{df[col].unique()}")


def check_df_summary(source: str):
    df = pd.read_csv(source)
    print(f"Info table\n{df.info()}")