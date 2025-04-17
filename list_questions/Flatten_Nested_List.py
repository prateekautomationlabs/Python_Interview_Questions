nested = [[1, 2], [3, 4], [5, 6]]
nested_deeply=[1, [2, [3, 4]],5]
#flattened = [1, 2, 3, 4, 5, 6]


#using 2 for loops
def flattened_list(nested):
    flattened=[]
    for sub_list in nested:
        for item in sub_list:
            flattened.append(item)

    return flattened

print(flattened_list(nested))


#in case of deeply nested list like nested_deep=[1, [2, [3, 4]]]

def flattened_deeply_list(nested_deeply):
    flattened_list=[]
    for item in nested_deeply:
        if isinstance(item,list):
            flattened_list.extend(flattened_deeply_list(item))
        else:
            flattened_list.append(item)

    return flattened_list



print(flattened_deeply_list(nested_deeply))