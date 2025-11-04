# roman_to_int.py

class RomanConverter:
    """
    A class to convert Roman numerals to integers.
    """

    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    @staticmethod
    def roman_to_int(roman: str) -> int:
        """
        Converts a Roman numeral string to an integer.
        """
        roman = roman.upper()
        total = 0
        prev_value = 0

        for char in reversed(roman):
            if char not in RomanConverter.roman_map:
                raise ValueError(f"Invalid Roman numeral: {char}")

            value = RomanConverter.roman_map[char]

            if value < prev_value:
                total -= value
            else:
                total += value

            prev_value = value

        return total


if __name__ == "__main__":
    # Example usage
    roman_input = input("Enter a Roman numeral: ")
    try:
        result = RomanConverter.roman_to_int(roman_input)
        print(f"{roman_input.upper()} = {result}")
    except ValueError as e:
        print(e)
