# input_str: hello how are you
#expected output: uoy era woh olleh

def reverse_words_with_sentence(input_str):
    reverse_lst = input_str.split()[::-1]
    reverse_words = [word[::-1] for word in reverse_lst]
    return " ".join(reverse_words)

input_str = "hello how are you"
print(reverse_words_with_sentence(input_str))
