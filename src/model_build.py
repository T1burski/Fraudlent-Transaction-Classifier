from data_ingestion import DataIngestion
from data_preprocessing import DataPreprocessor
from model_functions import ModelFunctions
import pickle

'''
this script adds together all modules in a pipeline to ingest
the data so, afterwards, we train the model.
Everytime the model needs to be retrained with new data,
run this script
'''

data_source = "data\df.parquet.gzip"

data = DataIngestion(data_path=data_source).load_data()

processed_data = DataPreprocessor(data).select_columns()

X = processed_data.drop("Class", axis=1)
y = processed_data["Class"]

clf_production = ModelFunctions().train_model(X, y)

# Saving the model to a pickle file to be used in production

with open('artifacts\model.pkl', 'wb') as model_file:
    pickle.dump(clf_production, model_file)