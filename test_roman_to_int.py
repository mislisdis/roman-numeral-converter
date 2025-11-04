# test_roman_to_int.py

import unittest
from roman_to_int import RomanConverter

class TestRomanConverter(unittest.TestCase):

    def test_basic_numbers(self):
        self.assertEqual(RomanConverter.roman_to_int("I"), 1)
        self.assertEqual(RomanConverter.roman_to_int("V"), 5)
        self.assertEqual(RomanConverter.roman_to_int("X"), 10)
        self.assertEqual(RomanConverter.roman_to_int("L"), 50)
        self.assertEqual(RomanConverter.roman_to_int("C"), 100)
        self.assertEqual(RomanConverter.roman_to_int("D"), 500)
        self.assertEqual(RomanConverter.roman_to_int("M"), 1000)

    def test_combinations(self):
        self.assertEqual(RomanConverter.roman_to_int("II"), 2)
        self.assertEqual(RomanConverter.roman_to_int("IV"), 4)
        self.assertEqual(RomanConverter.roman_to_int("IX"), 9)
        self.assertEqual(RomanConverter.roman_to_int("LVIII"), 58)
        self.assertEqual(RomanConverter.roman_to_int("MCMXCIV"), 1994)
        self.assertEqual(RomanConverter.roman_to_int("MMMCMXCIX"), 3999)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            RomanConverter.roman_to_int("ABC")

        with self.assertRaises(ValueError):
            RomanConverter.roman_to_int("VX")

if __name__ == "__main__":
    unittest.main()
