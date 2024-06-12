
sample_dict = {'apple': 20, 'banana': 10, 'orange': 30, 'grape': 5}


key_to_remove = 'banana'


if key_to_remove in sample_dict:
    del sample_dict[key_to_remove]


print("Updated Dictionary:", sample_dict)
