def reverse_array(arr):
    length = len(arr)
    for i in range(length // 2):
        temp = arr[i]
        arr[i] = arr[length - 1 - i]
        arr[length - 1 - i] = temp


def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()


array = [1, 2, 3, 4, 5]  

print("Original array:")
print_array(array)

reverse_array(array)

print("Reversed array:")
print_array(array)
