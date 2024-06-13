def find_repeated_items(t):
    repeated_items = []
    seen_items = []

    for item in t:
        if item in seen_items and item not in repeated_items:
            repeated_items.append(item)
        seen_items.append(item)

    return repeated_items


my_tuple = (1, 2, 3, 2, 4, 5, 3, 2, 6)


repeated_items = find_repeated_items(my_tuple)


print("Repeated items in the tuple:", repeated_items)
