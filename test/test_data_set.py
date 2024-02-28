import unittest
from unittest.mock import mock_open, patch

import sys
sys.path.append('../')
from src.data_set import data_set
from mock_data.mock_data_set import data

class TestDataCollection(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_data_set(self, mock_file_open):
        # Set up mock data to be read
        mock_file_open.return_value.__enter__ = lambda self: self
        mock_file_open.return_value.__iter__ = lambda self: iter(['\n'.join([','.join(entry) for entry in data])])

        # Call the function to collect data
        processed_data = data_set()

        # Check if the file is opened with the correct path and mode
        mock_file_open.assert_called_once_with("data/raw_data/train_and_test_data.csv", encoding="utf8")

        # Verify that the processed data has been collected correctly
        self.assertEqual(processed_data, data)

if __name__ == "__main__":
    unittest.main()
