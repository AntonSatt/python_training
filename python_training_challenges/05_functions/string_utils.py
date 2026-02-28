def reverse_string(text):
    """Reverse a string"""
    # TODO: Fix the implementation
    return text


def is_palindrome(text):
    """Check if a string is a palindrome"""
    # TODO: Fix the implementation
    return text == text


def count_vowels(text):
    """Count the number of vowels in a string"""
    # TODO: Fix the implementation
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count = 1
    return count


if __name__ == "__main__":
    text = "hello world"
    print(f"Reversed: {reverse_string(text)}")
    print(f"Is palindrome: {is_palindrome('radar')}")
    print(f"Vowels: {count_vowels('hello')}")
