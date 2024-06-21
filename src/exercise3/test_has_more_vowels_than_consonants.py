import pytest
from .has_more_vowels_than_consonants import has_more_vowels_than_consonants
import sys

sys.setrecursionlimit(1500)


@pytest.mark.parametrize(
    "test_input,expected",
    [
        # Edge cases
        ("", False),
        ("a", True),
        ("b", False),
        ("a" * 10, True),
        ("b" * 10, False),
        # General cases
        ("hello", False),
        ("hi", False),
        ("helloo", False),
        ("hiii", True),
        ("aeiou", True),
        # Mix of vowels and consonants
        ("apple", False),
        ("banana", False),
        ("xylophone", False),
        ("algorithm", False),
        ("openai", True),
        # Special characters and numbers
        ("hello123", False),
        ("!@#$%^", False),
        ("hello@world", False),
        # Upper case
        ("HELLO", False),
        ("AEIOU", True),
        ("Hello", False),
        # Non-English characters
        ("áéíóú", False),
        ("日本語", False),
        ("Привет", False),
        # Large input
        ("a" * 100 + "b" * 50, True),
        # Different combinations
        ("a!b@c#d$e", False),
        ("hello world", False),
        # Testing performance with large strings
        ("a" * 55 + "b" * 56, False),
        # Extreme edge cases
        ("b" * 200, False),
        ("a" * 300, True),
        # Additional cases for variety
        ("", False),
        (" ", False),
        ("ab" * 50, False),
        ("a" * 50 + "e" * 25 + "b" * 25, True),
        ("a" * 30 + "b" * 30 + "c" * 30 + "d" * 10, False),
        ("abcde" * 20, False),
        ("a" * 25 + "e" * 25 + "i" * 25 + "o" * 25, True),
        ("hello world!", False),
        ("a" * 500 + "!" * 500, True),
        ("a" * 500 + "e" * 250 + "b" * 250, True),
        ("abc" * 100, False),
        ("ab" * 250 + "cd" * 250, False),
        ("a" * 333 + "e" * 333 + "i" * 334, True),
        ("a" * 500 + "b" * 300 + "c" * 200, False),
        ("python", False),
        ("java", False),
        ("pythonista", False),
        ("machinelearning", False),
        ("deeplearning", False),
        ("ai", True),
    ],
)
def test_has_more_vowels_than_consonants(test_input, expected):
    assert has_more_vowels_than_consonants(test_input) == expected
