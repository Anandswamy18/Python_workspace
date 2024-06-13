def find_common_items(list1, list2):
  
    set1 = set(list1)
    set2 = set(list2)
    
  
    common_items = set1.intersection(set2)
    
    
    common_items_list = list(common_items)
    
    return common_items_list


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_items = find_common_items(list1, list2)
print("Common items between list1 and list2:", common_items)
