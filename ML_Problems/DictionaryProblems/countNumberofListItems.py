def count_items_in_list_values(d):
    count = 0 
     
    for value in d.values(): 
        if type(value) == list:  
            count += len(value) 
    return count  


sample_dict = {'a': [1, 2, 3], 'b': 'string', 'c': [4, 5,8,8,8]}


result = count_items_in_list_values(sample_dict)

print("Number of items in list values:", result)
