def remove_duplicates_from_list_of_lists(list_of_lists):
    seen = {}
    
    for sublist in list_of_lists:
       
        sublist_tuple = tuple(sublist)
        
        
        seen[sublist_tuple] = sublist
    
    
    result = list(seen.values())
    
    return result


sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]


new_list = remove_duplicates_from_list_of_lists(sample_list)


print("New List without duplicates:")
print(new_list)
