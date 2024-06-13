def sum_of_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


my_list = [1, 2, 3, 4, 5]
result = sum_of_list(my_list)
print("Sum of all items in the list:", result)
