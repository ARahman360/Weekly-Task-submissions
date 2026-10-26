import unittest
from unittest.mock import patch
import builtins

class TestMainProgram(unittest.TestCase):
    @patch('builtins.input', return_value='A7_T5_D1.csv')
    @patch('builtins.print')
    def test_main_output(self, mock_print, mock_input):
        import main  # This assumes main.py is in the same directory

        # Run the main function
        main.main()

        # Expected lines in output
        expected_lines = [
            "Program starting.",
            'Reading file "A7_T5_D1.csv".',
            "Analysing timestamps.",
            "Displaying results.",
            "### Electricity consumption summary ###",
            " - Monday usage 2510.00 kWh, cost 279.42 €",
            " - Tuesday usage 2364.00 kWh, cost 286.46 €",
            " - Wednesday usage 0.00 kWh, cost 0.00 €",
            " - Thursday usage 0.00 kWh, cost 0.00 €",
            " - Friday usage 0.00 kWh, cost 0.00 €",
            " - Saturday usage 0.00 kWh, cost 0.00 €",
            " - Sunday usage 0.00 kWh, cost 0.00 €",
            "### Electricity consumption summary ###",
            "Program ending."
        ]

        # Flatten the captured print calls
        printed_lines = [args[0] for args, _ in mock_print.call_args_list]

        # Check that each expected line is in the printed output
        for line in expected_lines:
            self.assertIn(line, printed_lines)

if __name__ == '__main__':
    unittest.main()

