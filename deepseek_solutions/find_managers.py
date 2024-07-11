import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # Group by managerId and count the number of direct reports
    manager_counts = employee.groupby('managerId').size().reset_index(name='report_count')
    
    # Filter managers with at least five direct reports
    managers_with_five_reports = manager_counts[manager_counts['report_count'] >= 5]
    
    # Merge with the original employee table to get the names of these managers
    result = employee[employee['id'].isin(managers_with_five_reports['managerId'])][['name']]
    
    return result