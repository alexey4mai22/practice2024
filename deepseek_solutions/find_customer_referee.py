import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame to include rows where referee_id is null or not equal to 2
    filtered_df = customer[(customer['referee_id'].isnull()) | (customer['referee_id'] != 2)]
    
    # Select only the 'name' column
    result_df = filtered_df[['name']]
    
    return result_df