import pandas as pd
import os

TRAINING_DATA = os.environ.get('train_file')
TESTING_DATA = os.environ.get('test_file')

if __name__ == '__main__':
    pass

    def read_file(file_path):
        dataFrame = pd.read_csv(file_path, na_values='?')
        return dataFrame
    
    train_raw = read_file(TRAINING_DATA)
    test_raw = read_file(TESTING_DATA)