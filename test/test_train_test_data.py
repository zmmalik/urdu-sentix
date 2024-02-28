import unittest
import pandas as pd
import sys
sys.path.append('../')
from src.train_test_data import split_data
from mock_data.mock_train_test_data import data

class TestTrainTestData(unittest.TestCase):

    def test_split_data(self):
        df = pd.DataFrame(data)
        train_data, test_data, train_labels, test_labels = split_data(df)
        self.assertIsNotNone(train_data)
        self.assertIsNotNone(train_labels)
        self.assertIsNotNone(test_data)
        self.assertIsNotNone(test_labels)
