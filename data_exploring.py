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

# now i want to get some info about the dataset
# insights:
# - how many columns and rows?
# - what's the name and datatype of each colum?
# - had any missing values?
# - the columns names could be renamed for better names or consistency?
# - basic statistics?


# i will display the first and last 10 rows of my dataset
print(df.head(10))
print(df.tail(10))

# now i will print the info
print(df.info)

# now i will print the columns names
print(df.columns)

# not i will see the data types
print(df.dtypes)
print(df.describe)

descriptive_stats_all = df.describe(include='all')
print(descriptive_stats_all)
