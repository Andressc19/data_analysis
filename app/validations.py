import pandas as pd

def check_column_na(dataframe):
    """
        function to check null values per column
    """
    print(f"Datos nulos por columna\n{dataframe.isnull().sum()}\n")


def check_unique(dataframe):
    """
        function to check unique values for each column
    """
    for col in dataframe.columns:
        print(f"Valores únicos en la columna '{col}':\n{dataframe[col].unique()}")


def check_df_summary(dataframe: str):
    """
        function to show dataframe's summary
    """
    df = pd.read_csv(dataframe)
    print(f"Info table\n{df.info()}")

