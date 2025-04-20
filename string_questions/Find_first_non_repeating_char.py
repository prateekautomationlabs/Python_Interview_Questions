#Given a string, find the first non-repeating character.
#input_str = "xayczxaybc"
#o/p z
from collections import Counter

def find_first_non_repeating_char(input_str):
    char_occurrance_count = Counter(input_str)

    for char in input_str:
        if char_occurrance_count[char]==1:
            return char

print(find_first_non_repeating_char("xayczxaybc"))

