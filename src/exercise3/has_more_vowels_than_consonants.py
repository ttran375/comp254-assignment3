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
        0
        if not s
        # Recursive case: check the first character of the string
        else (
            # Add 1 if the character is a vowel
            1
            if is_vowel(s[0])
            else 0
        )
        +
        # Call the function recursively on the rest of the string (s[1:])
        count_vowels(s[1:])
    )


def count_consonants(s):
    """
    Counts the number of consonants in a given string using recursion.
    """
    return (
        # Base case: If the string is empty, return 0
        0
        if not s
        # Recursive case:
        else (
            # Add 1 if the character is a consonant
            1
            if s[0].isalpha() and not is_vowel(s[0])
            else 0
        )
        +
        # Counting vowels in the rest of the string
        count_consonants(s[1:])
    )


def has_more_vowels_than_consonants(s):
    """
    Checks if a given string has more vowels than consonants.
    """
    # Compare the number of vowels and consonants in the string
    return count_vowels(s) > count_consonants(s)
