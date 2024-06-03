import pandas as pd


def load_data_from_file(file_path):
    """
    load data from a CSV file.

    parameters:
    file_path (str): the path to the CSV file. 

    returns:
    pd.dataframe: the loaded data as a pandas dataframe.
    """
    return pd.read_csv(file_path)
