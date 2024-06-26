def is_vowel(char):
    """
    Checks if the given character is a vowel (a, e, i, o, u).
    """
    # Convert the character to lowercase and check if it is in the string "aeiou"
    return char.lower() in "aeiou"


def count_vowels(s):
    """
    Counts the number of vowels in a given string using recursion.
    """
    return (
        # Base case: if the string is empty, return 0 (no vowels in an empty string)
        0 if not s

        # Recursive case: check the first character of the string
        else (
            # If it is a vowel, add 1 to the count, otherwise add 0
            1 if is_vowel(s[0]) else 0
        ) +
        # Call the function recursively on the rest of the string (s[1:])
        count_vowels(s[1:])
    )
