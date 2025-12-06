import pandas as pd

def normalize_to_upper(dataframe):
    """
        function to normalize to upper each string column value
    """
    for col in dataframe.select_dtypes(include="object"):
        dataframe[col] = dataframe[col].str.upper()
    return dataframe


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
        print(f"Valores únicos en la columna '{col}':\n{dataframe[col].unique()}\n")


def check_df_summary(dataframe: str):
    """
        function to show dataframe's summary
    """
    print(f"Información general del dataset \n{dataframe.info()}")