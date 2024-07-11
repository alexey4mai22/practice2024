import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    # Sort the DataFrame by visit_date
    stadium = stadium.sort_values('visit_date')

    # Calculate the difference between the current id and the next two ids
    stadium['diff1'] = stadium['id'].diff()
    stadium['diff2'] = stadium['id'].diff(2)

    # Filter the rows where the difference is 1
    stadium = stadium[(stadium['diff1'] == 1) & (stadium['diff2'] == 2)]

    # Remove the temporary columns
    stadium = stadium.drop(columns=['diff1', 'diff2'])

    # Filter the rows where the people count is >= 100
    stadium = stadium[stadium['people'] >= 100]

    # Sort the DataFrame by visit_date
    stadium = stadium.sort_values('visit_date')

    # Reset the index
    stadium = stadium.reset_index(drop=True)

    return stadium
