import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Filter out banned users
    unbanned_users = users[users['banned'] == 'No']
    
    # Filter trips where both client and driver are unbanned
    valid_trips = trips[
        (trips['client_id'].isin(unbanned_users['users_id'])) &
        (trips['driver_id'].isin(unbanned_users['users_id']))
    ]
    
    # Filter trips within the date range
    valid_trips = valid_trips[(valid_trips['request_at'] >= '2013-10-01') & (valid_trips['request_at'] <= '2013-10-03')]
    
    # Calculate the total number of trips and the number of canceled trips for each day
    total_trips = valid_trips.groupby('request_at').size().reset_index(name='total_trips')
    canceled_trips = valid_trips[valid_trips['status'].isin(['cancelled_by_driver', 'cancelled_by_client'])].groupby('request_at').size().reset_index(name='canceled_trips')
    
    # Merge the total and canceled trips dataframes
    result = pd.merge(total_trips, canceled_trips, on='request_at', how='left')
    result['canceled_trips'] = result['canceled_trips'].fillna(0)
    
    # Calculate the cancellation rate
    result['Cancellation Rate'] = (result['canceled_trips'] / result['total_trips']).round(2)
    
    # Rename columns to match the required output
    result.rename(columns={'request_at': 'Day'}, inplace=True)
    
    return result[['Day', 'Cancellation Rate']]