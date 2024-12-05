import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Group by managerId and count the number of employees in each department
    manager_counts = employee.groupby('managerId').size().reset_index(name='count')
    
    # Filter the managers with at least five direct reports
    managers = manager_counts[manager_counts['count'] >= 5]['managerId']
    
    # Join the managers with the Employee table to get their names
    result = employee[employee['id'].isin(managers)][['name']]
    
    return result
