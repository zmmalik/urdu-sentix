import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.user_interface import display_results

class TestUserInterface(unittest.TestCase):
    def test_display_results(self):
        mock_evaluation_results = {'confusion_matrix': [[10, 2], [3, 15]],
                                    'accuracy': 0.85}
        with StringIO() as buffer, redirect_stdout(buffer):
            display_results(mock_evaluation_results)
            output = buffer.getvalue()
