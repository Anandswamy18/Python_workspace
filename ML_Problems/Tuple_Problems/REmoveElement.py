def remove_item_from_tuple(t, item):
   
    new_tuple_list = []
    
  
    for elem in t:
       
        if elem != item:
            new_tuple_list.append(elem)
    
    
    new_tuple = tuple(new_tuple_list)
    
    return new_tuple


my_tuple = (1, 2, 3, 4, 5)
item_to_remove = 3


new_tuple = remove_item_from_tuple(my_tuple, item_to_remove)


print("Original tuple:", my_tuple)
print("Modified tuple:", new_tuple)
