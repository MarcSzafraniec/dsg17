import pandas as pd

def read_data(train_filename, test_filename):
	'''Opens train and test files. Data is comma separated.
	Drops 'sample_id' field from test

	Args:
		train_filename
		test_filename
	Returns:
		raw_train_dataset - pandas data from for train data.
		raw_test_datset - pandas data from for test data.
		SAMPLE_ID_TEST - sample ids for test data.
	'''
	raw_train_dataset = pd.read_csv(train_filename, sep = ",")
	raw_test_dataset = pd.read_csv(test_filename, sep = ",")
	SAMPLE_ID_TEST = raw_test_dataset['sample_id']
	raw_test_dataset.drop('sample_id',inplace=True,axis=1)

	return raw_train_dataset,raw_test_dataset,SAMPLE_ID_TEST