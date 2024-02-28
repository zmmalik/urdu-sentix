import unittest
from sklearn.metrics import accuracy_score
from src.accuracy_evaluation import evaluate_accuracy
from mock_data.mock_accuracy_evaluation import mock_test_labels, mock_nb_predictions, mock_rf_predictions, mock_dt_predictions

class TestEvaluateAccuracy(unittest.TestCase):
    def test_evaluate_accuracy(self):
        # Call the function to evaluate accuracy
        nb_accuracy_result, rf_accuracy_result, dt_accuracy_result = evaluate_accuracy(
            mock_test_labels, mock_nb_predictions, mock_rf_predictions, mock_dt_predictions
        )

        # Calculate accuracy scores using sklearn
        expected_nb_accuracy = accuracy_score(mock_test_labels, mock_nb_predictions)
        expected_rf_accuracy = accuracy_score(mock_test_labels, mock_rf_predictions)
        expected_dt_accuracy = accuracy_score(mock_test_labels, mock_dt_predictions)

        # Check if accuracy scores are calculated correctly
        self.assertEqual(nb_accuracy_result, expected_nb_accuracy)
        self.assertEqual(rf_accuracy_result, expected_rf_accuracy)
        self.assertEqual(dt_accuracy_result, expected_dt_accuracy)

if __name__ == "__main__":
    unittest.main()
