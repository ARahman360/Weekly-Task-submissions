import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Import from main.py
from main import TIMESTAMP, readTimestamps, displayTimestamps

class TestTimestampProgram(unittest.TestCase):
    def setUp(self):
        # These are relative to the project root (where GitHub Classroom runs tests)
        self.test_files = [
            ("A7_T4_D1.csv", 48),
            ("A7_T4_D2.csv", 168),
            ("A7_T4_D3.csv", 130)
        ]

    def test_read_and_display(self):
        for filename, expected_count in self.test_files:
            # Use absolute path from project root
            filepath = os.path.abspath(filename)
            timestamps = []
            readTimestamps(filepath, timestamps)
            self.assertEqual(len(timestamps), expected_count)

            captured_output = StringIO()
            sys.stdout = captured_output
            displayTimestamps(timestamps)
            sys.stdout = sys.__stdout__

            output_lines = captured_output.getvalue().strip().split('\n')
            self.assertEqual(len(output_lines) - 1, expected_count)  # Subtract header

            # Check formatting of first line
            self.assertTrue(output_lines[1].startswith(" - "))
            self.assertIn("price", output_lines[1])
            self.assertIn("consumption", output_lines[1])
            self.assertIn("total", output_lines[1])

if __name__ == '__main__':
    unittest.main()
