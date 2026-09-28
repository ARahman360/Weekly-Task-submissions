import unittest
import subprocess
import sys

class TestHexColorSlicing(unittest.TestCase):
    def test_output(self):
        # Simulated user input
        user_input = '#FFA500\n'

        # Run the student's script as a subprocess
        result = subprocess.run(
            [sys.executable, 'main.py'],
            input=user_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Normalize line endings
        output = result.stdout.replace('\r\n', '\n')

        # Expected output as printed by the student's code
        expected_output = (
            "Program starting.\n\n"
            "Insert a hex color: \n"
            "Colors\n"
            "- Red FF\n"
            "- Green A5\n"
            "- Blue 00\n\n"
            "Program ending.\n"
        )

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
