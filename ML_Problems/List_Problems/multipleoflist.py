def product_of_list(lst):
    product = 1
    for item in lst:
        
        product = product * item
    return product


my_list = [1, 2, 3, 4, 5]
result = product_of_list(my_list)
print("Product of all items in the list:", result)
