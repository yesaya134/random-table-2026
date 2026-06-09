import pandas as pd

DEFAULT_TABLE = "../data/example-table.csv"

# DEFAULT_TABLE = Path

def load_table(filepath = DEFAULT_TABLE):
    example_table = pd.read_csv(filepath)
    example_table.columns = example_table.columns.str.strip()
    return example_table

def categories(filepath = DEFAULT_TABLE):
    example_table = load_table(filepath)
    return example_table.columns.to_list()