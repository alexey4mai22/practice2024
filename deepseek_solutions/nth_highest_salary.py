import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Remove duplicate salaries
    unique_salaries = employee['salary'].drop_duplicates()
    
    # Sort the salaries in descending order
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    
    # Check if there are at least N unique salaries
    if len(sorted_salaries) >= N:
        nth_highest = sorted_salaries.iloc[N - 1]
    else:
        nth_highest = None
    
    # Return the result as a DataFrame
    return pd.DataFrame({'getNthHighestSalary(N)': [nth_highest]})