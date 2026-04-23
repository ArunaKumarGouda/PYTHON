# Step 2: Main Script (string_processor.py)

from string_helpers import reverse_string, count_vowels

def process_string(input_str):
    return reverse_string(input_str), count_vowels(input_str)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    reversed_str, vowels = process_string(user_input)

    print("Original:", user_input)
    print("Reversed:", reversed_str)
    print("Vowels:", vowels)
