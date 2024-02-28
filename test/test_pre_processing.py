import unittest
import sys
sys.path.append('../')
from src.pre_processing import preprocess_data
from mock_data.mock_pre_processing import data

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_data(self):
        preprocessed_data = preprocess_data([(entry["Comment"][0], entry["sentiment"]) for entry in data])
        self.assertFalse(preprocessed_data.empty)
        self.assertFalse(preprocessed_data.isnull().values.any())