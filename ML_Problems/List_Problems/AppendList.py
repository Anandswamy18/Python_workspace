def append_lists(list1, list2):
   
    list2.extend(list1)
    return list2


list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("List after appending list1 to list2:", append_lists(list1, list2))
