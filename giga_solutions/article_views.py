import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter the rows where the author_id and viewer_id are equal
    result = views[views['author_id'] == views['viewer_id']]

    # Sort the result by id in ascending order
    result = result.sort_values('author_id').reset_index(drop=True)

    return result