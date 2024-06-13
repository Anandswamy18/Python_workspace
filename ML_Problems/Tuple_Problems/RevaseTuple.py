my_tuple = (1, 2, 3, 4, 5)


reversed_tuple = ()


for i in range(len(my_tuple) - 1, -1, -1):
    reversed_tuple += (my_tuple[i],)


print("Original tuple:", my_tuple)
print("Reversed tuple:", reversed_tuple)
