from collections.abc import Callable
import pandas as pd
from pandas import DataFrame

def write_dataset(source: str | DataFrame, output: str, execute: Callable | None = None):
    """
    Function to load a dataset (from CSV or DataFrame), process it, and save output to file
    """
    
    # load dataframe
    if isinstance(source, str):
        df = pd.read_csv(source)
    else:
        df = source
    
    # apply callable function if provided
    if isinstance(execute, Callable):
        df = execute(df)
    
    # save output
    df.to_csv(output, index=False)
    return df