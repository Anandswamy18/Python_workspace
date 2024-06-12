my_set = {10, 20, 30, 40, 50}


max_value = float('-inf')  # Set initial maximum value to negative infinity
min_value = float('inf')   # Set initial minimum value to positive infinity

second_max=float('-inf')   # Set initial maximum value to negative infinity
second_min=float('inf')    # Set initial minimum value to positive infinity



for num in my_set:
    if num > max_value:
        second_max=max_value
        max_value = num
    elif num > second_max and num < max_value:
         second_max=num
         

    if num < min_value:
        second_min=min_value
        min_value = num
    elif num < second_min and num > second_min:
         second_min=num

# Display the maximum and minimum values
print("Maximum value in the set:", max_value)
print("Minimum value in the set:", min_value)


print("sec_Maximum value in the set:", second_max)
print("sec_Minimum value in the set:", second_min)
