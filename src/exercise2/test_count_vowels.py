import pytest
from .count_vowels import count_vowels


@pytest.mark.parametrize(
    "input_str, expected_count",
    [
        ("hello", 2),
        ("world", 1),
        ("", 0),
        ("AEIOU", 5),
        ("python", 1),
        ("beautiful", 5),
        ("rhythm", 0),
        ("aeiouAEIOU", 10),
        ("quick brown fox", 4),
        ("This is a test.", 4),
        ("WHY", 0),
        ("xyz", 0),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5),
        ("abcdefghijklmnopqrstuvwxyz", 5),
        ("qwertyuiopasdfghjklzxcvbnm", 5),
        ("1234567890", 0),
        ("vowels are AEIOU", 9),
        ("Vowels and consonants", 6),
        ("Uppercase and lowercase vowels", 11),
        ("A long string with multiple vowels to test the function", 15),
        ("Short", 1),
        ("Even shorter", 4),
        ("Almost no vowels", 5),
        ("Aeiou are all the vowels", 11),
        ("Checking for Y as a vowel", 7),
        ("Just a string of text", 5),
        ("One vowel", 4),
        ("Two vowels", 3),
        ("Three vowels", 4),
        ("Four vowels", 4),
        ("Five vowels", 4),
        ("No vowels", 3),
        ("Some vowels", 4),
        ("More vowels", 4),
        ("Most vowels", 3),
        ("Rhythm", 0),
        ("Myth", 0),
        ("Fry", 0),
        ("Sky", 0),
        ("Dry", 0),
        ("Try", 0),
        ("Ply", 0),
        ("Fly", 0),
        ("cry", 0),
        ("sly", 0),
        ("pry", 0),
        ("why", 0),
        ("Shy", 0),
        ("spy", 0),
        ("spry", 0),
    ],
)
def test_count_vowels(input_str, expected_count):
    assert count_vowels(input_str) == expected_count
