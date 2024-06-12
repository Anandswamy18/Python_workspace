# Create a frozenset
frozenset1 = frozenset({1, 2, 3, 4, 5})

# Display the frozenset
print("Frozenset 1:", frozenset1)

# Attempt to add an element to the frozenset (will raise an error)
try:
    frozenset1.add(6)
except AttributeError as e:
    print("Error:", e)

# Create another frozenset
frozenset2 = frozenset({4, 5, 6, 7, 8})

# Display the second frozenset
print("Frozenset 2:", frozenset2)

# Perform set operations with frozensets
intersection = frozenset1 & frozenset2
union = frozenset1 | frozenset2

# Display the intersection and union of the frozensets
print("Intersection of Frozenset 1 and Frozenset 2:", intersection)
print("Union of Frozenset 1 and Frozenset 2:", union)
