import unittest
import sys
sys.path.append('../')
from src.machine_learning import train_models
from mock_data.mock_machine_learning import mock_train_data, mock_test_data, mock_train_labels, mock_test_labels

class TestTrainModels(unittest.TestCase):
    def test_train_models(self):
        # Call the function to train models
        test_labels, nb_predictions, rf_predictions, dt_predictions, nb_report, rf_report, dt_report = train_models(
            mock_train_data, mock_test_data, mock_train_labels, mock_test_labels
        )

        # Check if test labels are returned correctly
        self.assertEqual(test_labels, mock_test_labels)

        # Check if the length of predictions matches the length of test data
        self.assertEqual(len(nb_predictions), len(mock_test_data))
        self.assertEqual(len(rf_predictions), len(mock_test_data))
        self.assertEqual(len(dt_predictions), len(mock_test_data))

        # Check if classification reports are generated
        self.assertIsInstance(nb_report, str)
        self.assertIsInstance(rf_report, str)
        self.assertIsInstance(dt_report, str)

if __name__ == "__main__":
    unittest.main()
