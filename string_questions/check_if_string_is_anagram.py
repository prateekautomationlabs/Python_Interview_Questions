#silent as listen
#Key rules
#all characters are present
#same occurrence of characters
#no extra character
#case insensitivity

from collections import Counter
def check_string_for_anagram(source_str, target_str):
    source_occurrence_count = Counter(source_str.lower())
    target_occurrence_count = Counter(target_str.lower())

    if source_occurrence_count == target_occurrence_count:
        return True
    else:
        return False


print(check_string_for_anagram("silent","listen"))


#with regular expression

import re
def clean_text(input_str):
    return re.sub(r"[^a-z]","", input_str.lower())

def check_string_is_anagram_using_regex(str1, str2):
    return Counter(clean_text(str1)) == Counter(clean_text(str2))

print(check_string_is_anagram_using_regex("Dormitory!","Dirty room."))