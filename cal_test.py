import builtins
import unittest
from calculator import select_operation, get_float_input

class TestSelectOperation(unittest.TestCase):
    def test_select_addition(self):
        self.assertEqual(select_operation('+'), 'addition')

    def test_select_subtraction(self):
        self.assertEqual(select_operation('-'), 'subtraction')

    def test_select_multiplication(self):
        self.assertEqual(select_operation('*'), 'multiplication')

    def test_select_division(self):
        self.assertEqual(select_operation('/'), 'division')

    def test_select_power(self):
        self.assertEqual(select_operation('^'), 'power')

    def test_select_remainder(self):
        self.assertEqual(select_operation('%'), 'remainder')

    def test_select_terminate(self):
        self.assertEqual(select_operation('#'), 'terminate')

    def test_select_reset(self):
        self.assertEqual(select_operation('$'), 'reset')

    def test_select_invalid(self):
        self.assertEqual(select_operation('x'), 'invalid')

class TestGetFloatInput(unittest.TestCase):
    def test_get_valid_float_input(self):
        # Simulate user input using a list and a lambda function
        inputs = ['12.34']
        original_input = builtins.input
        builtins.input = lambda _: inputs.pop(0)
        self.assertEqual(get_float_input("Enter a number: "), 12.34)

    def test_get_invalid_float_input(self):
        # Simulate user input using a list and a lambda function
        inputs = ['not_a_number', '12.34']
        original_input = builtins.input
        builtins.input = lambda _: inputs.pop(0)
        self.assertEqual(get_float_input("Enter a string: "), 12.34)

if __name__ == "__main__":
    unittest.main()
