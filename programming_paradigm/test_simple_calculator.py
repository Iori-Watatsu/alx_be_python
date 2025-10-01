import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test add method"""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtraction(self):
        """Test subtract method"""
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        """Test multiply method"""
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        """Test divide method"""
        self.assertEqual(self.calc.divide(6, 3), 2)


if __name__ == "__main__":
    unittest.main()
