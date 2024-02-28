import unittest
import pandas as pd
import sys
sys.path.append('../')
from src.feature_extraction import extract_features
from mock_data.mock_feature_extraction import data

class TestFeatureExtraction(unittest.TestCase):

    def test_extract_features(self):
        df = pd.DataFrame(data)
        features = extract_features(df)
        self.assertIsNotNone(features)
