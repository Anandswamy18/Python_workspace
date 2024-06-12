def get_unique_values(dict_list):
    unique_values = set()  
    
    for dictionary in dict_list:
        for value in dictionary.values():
            unique_values.add(value)  
    return unique_values


sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
               {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]


unique_values = get_unique_values(sample_data)


print("Unique Values:", unique_values)
