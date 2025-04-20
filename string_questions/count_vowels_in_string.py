

input_str = "aeiouAEITOU"

#count number of vowels in a string

def count_number_of_vowels(input_str):
    vowels_str = "aeiou"
    counter=0
    return sum(1 for ch in input_str if ch.lower() in vowels_str)


print(count_number_of_vowels(input_str))