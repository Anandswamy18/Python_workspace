def remove_first_occurrence(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            arr.pop(i)
            break
    return arr


array = [1, 2, 3, 4, 2, 5]
element_to_remove = int(input("Enter a number to remove of its first occurance: "))
result = remove_first_occurrence(array, element_to_remove)
print("Array after removing the first occurrence of", element_to_remove, ":", result)
