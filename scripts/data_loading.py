import pandas as pd


def load_data_from_file(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file. 

    Returns:
    pd.DataFrame: The loaded data as a Pandas DataFrame.
    """
    return pd.read_csv(file_path)
