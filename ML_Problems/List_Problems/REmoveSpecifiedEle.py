sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


indices_to_remove = [0, 4, 5]
result_list = []

for i in range(len(sample_list)):
    if i not in indices_to_remove:
        result_list.append(sample_list[i])


print("Resulting List:", result_list)
