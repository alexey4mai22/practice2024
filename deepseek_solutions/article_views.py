import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter the rows where the author_id is equal to the viewer_id
    own_view_authors = views[views['author_id'] == views['viewer_id']]
    
    # Select the unique author_ids from the filtered rows
    unique_authors = own_view_authors['author_id'].unique()
    
    # Create a DataFrame with the unique author_ids
    result_df = pd.DataFrame(unique_authors, columns=['id'])
    
    # Sort the result DataFrame by id in ascending order
    result_df = result_df.sort_values(by='id').reset_index(drop=True)
    
    return result_df