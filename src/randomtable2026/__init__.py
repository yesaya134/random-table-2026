import pandas as pd

def load_table(filepath):
    example_table = pd.read_csv(filepath)
    example_table.columns = example_table.columns.str.strip()
    return example_table