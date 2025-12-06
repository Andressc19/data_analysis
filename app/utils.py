import pandas as pd
from pandas import DataFrame

def write_dataset(source: str, output: str, execute):
    """
        function to write a dataset an return output file
    """
    df: DataFrame = pd.read_csv(source)
    df = execute(df)
    df.to_csv(output)