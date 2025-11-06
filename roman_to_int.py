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

    # Invalid subtractive or positional combinations (not allowed in Roman numerals)
    invalid_pairs = {
        "IL", "IC", "ID", "IM",  # I can only precede V or X
        "XD", "XM",              # X can only precede L or C
        "VX", "LC", "DM",        # These orders are invalid
        "VV", "LL", "DD"         # Repeated V, L, or D are invalid
    }

    @staticmethod
    def roman_to_int(roman: str) -> int:
        """
        Converts a Roman numeral string to an integer.
        Raises ValueError for invalid numerals.
        """
        roman = roman.strip().upper()

        # Empty input check
        if not roman:
            raise ValueError("Empty Roman numeral not allowed.")

        # Character validity check
        for char in roman:
            if char not in RomanConverter.roman_map:
                raise ValueError(f"Invalid Roman numeral character: {char}")

        # Check invalid two-character combinations
        for i in range(len(roman) - 1):
            pair = roman[i:i + 2]
            if pair in RomanConverter.invalid_pairs:
                raise ValueError(f"Invalid Roman numeral combination: {pair}")

        # Check for too many repeats (more than 3 in a row)
        if "IIII" in roman or "XXXX" in roman or "CCCC" in roman or "MMMM" in roman:
            raise ValueError("Invalid repetition: numerals repeated more than 3 times.")

        total = 0
        prev_value = 0

        for char in reversed(roman):
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
        print("Error:", e)
