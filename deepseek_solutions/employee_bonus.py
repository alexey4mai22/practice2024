import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Merge the Employee and Bonus tables on empId
    merged_df = pd.merge(employee, bonus, on='empId', how='left')
    
    # Filter the merged dataframe to include only rows where bonus is less than 1000 or null
    result_df = merged_df[merged_df['bonus'].isnull() | (merged_df['bonus'] < 1000)]
    
    # Select only the 'name' and 'bonus' columns
    result_df = result_df[['name', 'bonus']]
    
    return result_df