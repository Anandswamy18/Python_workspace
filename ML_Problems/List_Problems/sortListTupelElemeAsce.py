def sort_by_last_element(tuples_list):
    def last_element(tuple):
        return tuple[-1]

    
    sorted_list = sorted(tuples_list, key=last_element)
    return sorted_list


sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sort_by_last_element(sample_list)
print("Expected Result:", result)
