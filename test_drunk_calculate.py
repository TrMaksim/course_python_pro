import unittest
from io import StringIO
from unittest.mock import patch
from drunk_polish_calculator import op_plus, op_minus, op_multiply, op_divide, main


class CalculatorTestCase(unittest.TestCase):
    def test_op_plus(self):
        test_cases = [
            (2, 2, 4.0),
            (5, 5, 10.0),
            (7, 8, 15.0)
        ]
        for x, y, expected in test_cases:
            result = op_plus(x, y)
            self.assertEqual(result, expected)
    def test_op_minus(self):
        test_cases = [
            (2, 3, 1.0),
            (4, 2, -2.0),
            (5, 10, 5.0),
        ]
        for y, x, expected in test_cases:
            result = op_minus(y, x)
            self.assertEqual(result, expected)

    def test_op_multiply(self):
        test_cases = [
            (2, 2, 4.0),
            (5, 5, 25.0),
            (10, 2, 20.0)
        ]
        for x, y, expected in test_cases:
            result = op_multiply(x, y)
            self.assertEqual(result, expected)

    def test_op_divide(self):
        test_cases = [
            (2, 4, 2.0),
            (4, 2, 0.5),
            (5, 10, 2.0),
        ]
        for x, y, expected in test_cases:
            result = op_divide(y, x)
            self.assertEqual(result, expected)

class TestMain(unittest.TestCase):
    def test_main(self):

        input_string = "2 2 + 4 5 * / 4 2 -"
        expected_output = 5.0

        with unittest.mock.patch('builtins.input', return_value=input_string):

            with unittest.mock.patch('builtins.print') as mock_print:
                main()

                mock_print.assert_called_with(expected_output)


if __name__ == '__main__':
    unittest.main()
