import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate salaries
    unique_salaries = employee['salary'].drop_duplicates()
    
    # Sort the salaries in descending order
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    
    # Check if there is a second highest salary
    if len(sorted_salaries) > 1:
        second_highest = sorted_salaries.iloc[1]
    else:
        second_highest = None
    
    # Return the result as a DataFrame
    return pd.DataFrame({'SecondHighestSalary': [second_highest]})