import pandas as pd

def unbanned_cancellation_rate(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Filter the trips where both the client and driver are not banned
    unbanned_trips = trips[~trips['client_id'].isin(users[users['banned'] == 'Yes']['users_id']) &
                           ~trips['driver_id'].isin(users[users['banned'] == 'Yes']['users_id'])]
    
    # Filter the unbanned trips within the specified date range
    unbanned_trips_range = unbanned_trips[(unbanned_trips['request_at'] >= '2013-10-01') &
                                         (unbanned_trips['request_at'] <= '2013-10-03')]
    
    # Calculate the cancellation rate for each day
    cancellation_rate = unbanned_trips_range.groupby('request_at').apply(lambda x: (x['status'] != 'completed').sum() / x.shape[0]).reset_index(name='Cancellation Rate')
    
    # Round the cancellation rate to two decimal points
    cancellation_rate['Cancellation Rate'] = cancellation_rate['Cancellation Rate'].round(2)
    
    return cancellation_rate
