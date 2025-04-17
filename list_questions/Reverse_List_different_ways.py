
list_numbers = [1,2,3,4,5]
#list_numbers = [5,4,3,2,1]

# #Using Slicing
# reverse_list_numbers= list_numbers[::-1]
# print(reverse_list_numbers)
#
# #Using reverse method
# list_numbers.reverse()
# print(list_numbers)

#Using temp variable
mid=len(list_numbers)//2
start=0
end=len(list_numbers)-1
temp =0

while end > mid:
    temp = list_numbers[start]
    list_numbers[start]=list_numbers[end]
    list_numbers[end] = temp
    start+=1
    end-=1

print(list_numbers)

list_numbers_with_insert = [1,2,3,4,5]
#Using insert method
reverse_list_with_insert = []
for item in list_numbers_with_insert:
    reverse_list_with_insert.insert(0,item)
print(reverse_list_with_insert)
