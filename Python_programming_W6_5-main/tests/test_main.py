import unittest
from main import readValues, analyseValues

class TestNumberAnalysis(unittest.TestCase):

    def test_file_1(self):
        values = readValues("A6_T5_D1.txt")
        result = analyseValues(values)
        expected = "Count;Sum;Greatest;Average\n2;53;43;26.50\n"
        self.assertEqual(result, expected)

    def test_file_2(self):
        values = readValues("A6_T5_D2.txt")
        result = analyseValues(values)
        expected = "Count;Sum;Greatest;Average\n10;508;91;50.80\n"
        self.assertEqual(result, expected)

    def test_file_3(self):
        values = readValues("A6_T5_D3.txt")
        result = analyseValues(values)
        expected = "Count;Sum;Greatest;Average\n100;5608;98;56.08\n"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

