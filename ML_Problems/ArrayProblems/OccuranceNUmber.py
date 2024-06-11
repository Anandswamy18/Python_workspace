def occurance_of_number(arr, number):
    length = len(arr)
    count = 0

    for i in range(length):
        if arr[i] == number:
            count += 1
    
    return count

array = [1, 2, 3, 4,1]
number = int(input("Enter a number to check its occurance: "))
result = occurance_of_number(array, number)
print("Occurrence of", number, "in the array:", result)
