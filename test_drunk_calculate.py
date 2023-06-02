import unittest
from io import StringIO
import builtins
from drunk_polish_calculator import op_plus, op_minus, op_multiply, op_divide, main


class CalculatorTestCase(unittest.TestCase):
    def test_op_plus(self):
        result = op_plus(2, 3)
        self.assertEqual(result, 5)

    def test_op_minus(self):
        result = op_minus(3, 2)
        self.assertEqual(result, -1)

    def test_op_multiply(self):
        result = op_multiply(2, 3)
        self.assertEqual(result, 6)

    def test_op_divide(self):
        result = op_divide(6, 3)
        self.assertEqual(result, 2)

    def test_main(self):
        input_string = "2 2 + 4 5 * / 4 2 -\n"
        expected_output = "5.0"

        stdin = StringIO(input_string)
        stdout = StringIO()

        original_input = builtins.input
        original_print = builtins.print
        builtins.input = lambda _: stdin.readline().rstrip('\n')
        builtins.print = lambda *args, **kwargs: original_print(*args, file=stdout, **kwargs)

        main()

        builtins.input = original_input
        builtins.print = original_print

        output = stdout.getvalue().strip()
        self.assertEqual(output, expected_output)
        self.assertEqual(stdin.readline(), "")


if __name__ == '__main__':
    unittest.main()
