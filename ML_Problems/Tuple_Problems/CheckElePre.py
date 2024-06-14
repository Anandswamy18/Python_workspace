def check_element_in_tuple(t, element):
    return element in t


my_tuple = (1, 2, 3, 4, 5)


element_to_check = 8


if check_element_in_tuple(my_tuple, element_to_check):
    print(f"Element {element_to_check} exists in the tuple.")
else:
    print(f"Element {element_to_check} does not exist in the tuple.")
