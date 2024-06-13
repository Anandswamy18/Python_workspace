def find_smallest_number(lst):
    if len(lst) == 0:
        return None  

    smallest = lst[0]  
    for num in lst:
        if num < smallest:
            smallest = num  
    return smallest

# Example usage
my_list = [5, 3, 9, 1, 4]
result = find_smallest_number(my_list)
print("The smallest number in the list is:", result)
