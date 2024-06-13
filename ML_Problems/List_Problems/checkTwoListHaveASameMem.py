def have_common_member(list1, list2):
    
    for item in list1:
      
        if item in list2:
            
            return True
    
    return False


list1 = [1, 2, 3, 4, 10,"anand"]
list2 = [5, 6, 7, 8, 9,"annd"]


result = have_common_member(list1, list2)


print("The lists have at least one common member:", result)
