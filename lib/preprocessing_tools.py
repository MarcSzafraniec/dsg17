import pandas as pd

def drop_data_with_small_duration(dataframe):
    '''Drop data with duration <= 30 sec and is_listened == 1
    '''
    dataframe = dataframe.drop(dataframe.index[(dataframe['media_duration'] <= 30)*(dataframe['is_listened'] == 1)],
                               axis = 0)
    return dataframe
def drop_songs_with_invalide_release_date(dataframe):
    '''Drop songs with release date late than 2019 year
    '''
    return dataframe[dataframe['release_date'] < 20190000]
def preprocess_data(train_dataframe, test_dataframe):
    '''Do all the preprocessing.
    '''
    preprocessed_train_dataset = train_dataframe
    preprocessed_test_dataset = test_dataframe
    
    preprocessed_train_dataset = drop_data_with_small_duration(preprocessed_train_dataset)
    
    preprocessed_train_dataset = drop_songs_with_invalide_release_date(preprocessed_train_dataset)
    preprocessed_test_dataset = drop_songs_with_invalide_release_date(preprocessed_test_dataset)
    
    return preprocessed_train_dataset, preprocessed_test_dataset
    
def get_merged_datasets(train_dataframe, test_dataframe):
    '''Merges vertically train over test dataframe.
    '''
    merged_datasets = train_dataframe.drop('is_listened', axis = 1).append(test_dataframe)
    merged_datasets = merged_datasets.reset_index()
    merged_datasets = merged_datasets.drop('index', axis=1)

    return merged_datasets