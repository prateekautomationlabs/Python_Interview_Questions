
"""
    This method will find the second largest number in the list
    """
def find_second_max(list_numbers):

    max_number = max(list_numbers)
    second_max=float("-inf") # handling for if all numbers are negative

    for number in list_numbers:
        if number < max_number and number > second_max:
            second_max=number

    return second_max


#using set and sort method
def find_second_max(list_numbers):
    unique_list = list(set(list_numbers))
    unique_list.sort()
    #conditional expression or a ternary operator in Python
    return unique_list[-2] if len(unique_list) >=2 else None

if __name__ == '__main__':
    list_numbers =[-5,-9,-4,-2,-8]
    print(find_second_max(list_numbers))



