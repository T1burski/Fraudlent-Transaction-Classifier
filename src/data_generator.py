import pandas as pd
import numpy as np
import random
import json

'''
this model exists only to generate data (transactions) to be used
in production and to test the model with "real" data.
'''

class DataGenerator:
    def __init__(self, rows):
        self.rows = rows
        self.min_max_dict = json.load(open("data\data_generator.json"))
    
    def generate_df(self):
        '''
        generates the data based on the max and min values
        of each feature
        '''
        df_data = pd.DataFrame(columns=['V4', 'V10', 'V12', 'V14', 'V20'])
        for c in df_data.columns:
            val = []
            for i in range(self.rows):
                val.append(random.uniform(self.min_max_dict[c][0], self.min_max_dict[c][1]))
            df_data[c] = val
        
        return df_data

if __name__ == "__main__":

    '''
    when this script is executed directly,
    it generates the min and max values for
    each feature to be used afterwards
    '''

    df = pd.read_parquet("data\df.parquet.gzip")
    df = df[['V4', 'V10', 'V12', 'V14', 'V20']]

    dict_mm = {}

    for c in df.columns:
        mm_list = []
        mm_list.append(np.min(df[c].values))
        mm_list.append(np.max(df[c].values))
        dict_mm[c] = mm_list

    with open("data\data_generator.json", "w") as json_file:
        json.dump(dict_mm, json_file)