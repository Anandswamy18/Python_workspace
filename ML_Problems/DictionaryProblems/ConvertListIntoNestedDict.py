def list_to_nested_dict(keys_list):
    nested_dict = {}
    current_dict = nested_dict
    
    
    for key in keys_list:
        
        current_dict[key] = {}
        
        current_dict = current_dict[key]
    
    return nested_dict


sample_list = ['Anand', 'Swamy', 'Regular', 'ROutine']


nested_dict = list_to_nested_dict(sample_list)

print(nested_dict)
