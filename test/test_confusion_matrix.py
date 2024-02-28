import unittest
import pandas as pd
import sys
sys.path.append('../')
from src.confusion_matrix import evaluate_models
from mock_data.mock_confusion_matrix import mock_test_labels, mock_nb_predictions, mock_rf_predictions, mock_dt_predictions

class TestEvaluateModels(unittest.TestCase):
    def test_evaluate_models(self):
        # Call the function to evaluate models
        nb_confusion_result, rf_confusion_result, dt_confusion_result = evaluate_models(
            mock_test_labels, mock_nb_predictions, mock_rf_predictions, mock_dt_predictions
        )

        # Check if the shape of confusion matrices is correct
        expected_classes = mock_test_labels.unique()
        self.assertEqual(nb_confusion_result.shape, (len(expected_classes), len(expected_classes)))
        self.assertEqual(rf_confusion_result.shape, (len(expected_classes), len(expected_classes)))
        self.assertEqual(dt_confusion_result.shape, (len(expected_classes), len(expected_classes)))

if __name__ == "__main__":
    unittest.main()
