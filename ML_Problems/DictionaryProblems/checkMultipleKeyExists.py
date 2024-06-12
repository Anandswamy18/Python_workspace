def check_keys_exist(d, keys):

    for key in keys:
        if key not in d:
            return False
    return True


sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


keys_to_check = ['a', 'c']


result = check_keys_exist(sample_dict, keys_to_check)

if result:
    print("All keys exist in the dictionary")
else:
    print("Not all keys exist in the dictionary")
