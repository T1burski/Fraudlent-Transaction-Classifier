'''
module created to preprocess the data for the model's training.
the features selected were chosen based on the study shown in the 
exploratory data analysis (EDA)
'''

class DataPreprocessor:
    def __init__(self, data):
        self.raw_data = data
        self.processed_data = None

    def select_columns(self):
        selected_columns = ['V4', 'V10', 'V12', 'V14', 'V20', 'Class']
        self.processed_data = self.raw_data[selected_columns]
        self.processed_data.drop_duplicates(inplace=True)

        return self.processed_data
