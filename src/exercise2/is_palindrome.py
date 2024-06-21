def is_palindrome(s):
    s = "".join(char for char in s if char.isalnum()).lower()
    return len(s) <= 1 or (s[0] == s[-1] and is_palindrome(s[1:-1]))


def main():
    s = input("Provide string entries to be checked: ").strip()
    print(is_palindrome(s))


if __name__ == "__main__":
    main()
