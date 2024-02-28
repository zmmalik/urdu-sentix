import unittest
import pandas as pd
from unittest.mock import patch, call
from src.save_result_to_csv import save_results
from mock_data.mock_save_result_to_csv import (
    mock_nb_confusion_result, mock_rf_confusion_result, mock_dt_confusion_result,
    mock_nb_accuracy_result, mock_rf_accuracy_result, mock_dt_accuracy_result,
    mock_nb_classification_report, mock_rf_classification_report, mock_dt_classification_report
)

class TestSaveResultToCSV(unittest.TestCase):
    @patch('src.save_result_to_csv.pd.DataFrame.to_csv')
    def test_save_results(self, mock_to_csv):
        # Call the function to save results
        save_results(
            mock_nb_confusion_result, mock_rf_confusion_result, mock_dt_confusion_result,
            mock_nb_accuracy_result, mock_rf_accuracy_result, mock_dt_accuracy_result,
            mock_nb_classification_report, mock_rf_classification_report, mock_dt_classification_report
        )

        # Assert calls to to_csv
        expected_calls = [
            call('data/results/accuracy.csv', index=False),
            call('data/results/confusion_matrices.csv', index=False),
            call('data/results/classification_report.csv', index=False)
        ]
        self.assertEqual(mock_to_csv.call_args_list, expected_calls)

if __name__ == "__main__":
    unittest.main()
