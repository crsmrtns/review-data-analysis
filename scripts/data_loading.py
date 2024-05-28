import pandas as pd

df = pd.read_csv(
    '/Users/cristianemartins/Desktop/portfolio/review-data-analysis/scripts/hm-cardigans-reviews.csv')
print(df)


def load_data_from_file(df):
    """
    load data from a CSV file

    parameters:
    file_path (str): the path to the CSV file

    returns:
    pd.DataFrame: the loaded data as a pandas dataframe
    """
    return pd.read_csv(df)
