import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Filter the rows where the referee_id is not 2 or null
    result = customer[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())]['name']

    return result
