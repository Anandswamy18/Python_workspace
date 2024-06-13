def list_difference_using_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    difference = list(set1 - set2)
    return difference


list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6]
print("List difference using sets:", list_difference_using_sets(list1, list2))
