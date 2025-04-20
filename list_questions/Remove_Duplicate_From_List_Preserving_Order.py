
list_numbers = [2,5,2,6,9,8,6]
#expected output after removing duplicate and preserving the order is: [2,5,6,9,8]

def get_unique_list_with_order_preserved(list_numbers):
    result = []
    seen=set()

    for item in list_numbers:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

print(get_unique_list_with_order_preserved(list_numbers))

