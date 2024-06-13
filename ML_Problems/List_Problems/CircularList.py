def are_circularly_identical(list1, list2):
  
    if len(list1) != len(list2):
        return False
    
   
    n = len(list1)
    for i in range(n):
        rotated_list1 = list1[i:] + list1[:i]
        if rotated_list1 == list2:
            return True
    
    
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 1, 2]

if are_circularly_identical(list1, list2):
    print("Lists are circularly identical.")
else:
    print("Lists are not circularly identical.")
