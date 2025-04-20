#For a gievn string , find total number of unique substring

#using 2 for loops
def get_unique_sub_str(input_str):
    unique_sub_set=set()
    for i in range(len(input_str)):
        for j in range((i+1),len(input_str)+1):
            unique_sub_set.add(input_str[i:j])
    return unique_sub_set


print(get_unique_sub_str("abc"))
