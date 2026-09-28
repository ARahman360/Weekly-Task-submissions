import unittest
import subprocess
import sys

class TestCompoundWordAnalysis(unittest.TestCase):
    def test_output_contains_expected_lines(self):
        user_input = 'Starflower\n0\n4\n1\n'

        result = subprocess.run(
            [sys.executable, 'main.py'],
            input=user_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout.replace('\r\n', '\n')  # Normalize line endings

        # Check for key expected lines (not full exact match)
        expected_lines = [
            "Program starting.",
            "The word you inserted is 'Starflower' and in reverse it is 'rewolfratS'.",
            "The inserted word length is 10",
            "Last character is 'r'",
            "Take substring from the inserted word by inserting...",
            "The word 'Starflower' sliced to the defined substring is 'Star'.",
            "Program ending."
        ]

        for line in expected_lines:
            self.assertIn(line, output)

if __name__ == '__main__':
    unittest.main()
