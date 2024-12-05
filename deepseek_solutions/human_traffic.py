import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where people >= 100
    filtered_stadium = stadium[stadium['people'] >= 100]
    
    if len(filtered_stadium) < 3:
        return pd.DataFrame(columns=stadium.columns)
    
    # Identify groups of consecutive ids
    filtered_stadium['group'] = (filtered_stadium['id'] != filtered_stadium['id'].shift() + 1).cumsum()
    
    # Filter groups with at least 3 consecutive ids
    result = filtered_stadium.groupby('group').filter(lambda x: len(x) >= 3)
    
    # Drop the group column and sort by visit_date
    result = result.drop(columns=['group']).sort_values(by='visit_date')
    
    return result