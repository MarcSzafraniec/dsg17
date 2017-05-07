import numpy as np
import pandas as pd
def print_data_stats(dataframe, prefix='Train'):
    print prefix+' Data stats'
    unique_analysis_columns = ['genre_id',
                               'media_id',
                               'album_id',
                               'context_type',
                               'platform_name',
                               'platform_family',
                               'listen_type',
                               'user_gender',
                               'user_id',
                               'artist_id',
                               'user_age']
    data_size = float(np.size(dataframe.index))
    
    print 'Overall size of data: ', data_size
    
    for col in unique_analysis_columns:
        col_unique_size = float(np.size(dataframe[col].unique()))
        print 'Unique values of '+col+' ', col_unique_size, ' which is ', float(col_unique_size) / float(data_size) * 100.0, '%'                                                   
    
    ages_to_check = xrange(18, 32)
    
    for age in ages_to_check:
        print 'Percentage of people yonger than', age, ' is equal to ', float(np.size(dataframe[dataframe['user_age'] < age].index)) / float(data_size) * 100.0, '%'