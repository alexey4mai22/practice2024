import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.sort_values('salary', ascending=False)
    employee = employee.drop_duplicates('salary')
    if len(employee) < N:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})': [employee.iloc[N-1]['salary']]})

# Test the function
employee = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
print(nth_highest_salary(employee, 2))

employee = pd.DataFrame({'id': [1], 'salary': [100]})
print(nth_highest_salary(employee, 2))
