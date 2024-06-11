def ascending_sort_dict_by_value(d):
    items = list(d.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:
                temp = items[j]
            items[j] = items[j + 1]
            items[j + 1] = temp
    return dict(items)


my_dict = {'apple': 20, 'banana': 10, 'orange': 30, 'grape': 5}


sorted_dict = ascending_sort_dict_by_value(my_dict)


print("Dictionary sorted by value in ascending order:", sorted_dict)
