def is_palindrome(s):
    """
    Checks if a given string is a palindrome using recursion.
    """
    # Remove non-alphanumeric characters and  convert all letters to lowercase
    s = "".join(char for char in s if char.isalnum()).lower()

    return (
        # Base case: If the string length is 1 or 0, it's a palindrome
        len(s) <= 1
        or
        # Recursive case: Check if the first and last characters of the string are the same
        (s[0] == s[-1] and is_palindrome(s[1:-1]))
    )
