def is_vowel(char):
    return char.lower() in "aeiou"


def count_vowels(s):
    return 0 if not s else (1 if is_vowel(s[0]) else 0) + count_vowels(s[1:])


def main():
    user_input = input("Enter a string: ")
    num_vowels = count_vowels(user_input)
    print(f"The number of vowels in the string is: {num_vowels}")


if __name__ == "__main__":
    main()
