import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    # Merge the two tables on the empId column
    merged = pd.merge(employee, bonus, how='left', on='empId')
    
    # Filter the rows where the bonus is less than 1000
    result = merged[merged['bonus'] < 1000][['name', 'bonus']]
    
    return result
