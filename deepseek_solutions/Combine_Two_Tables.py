import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # Perform a left join on 'personId'
    result_df = person.merge(address, on='personId', how='left')
    
    # Select the desired columns
    result_df = result_df[['firstName', 'lastName', 'city', 'state']]
    
    return result_df