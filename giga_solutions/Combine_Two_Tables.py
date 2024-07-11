import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Merge the two tables on personId
    combined_table = pd.merge(person, address, on='personId', how='left')
    
    # Return the combined table
    return combined_table
