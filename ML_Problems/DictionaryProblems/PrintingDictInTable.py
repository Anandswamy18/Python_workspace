sample_dict = {'Name': 'Anand', 'Age': 24, 'City': 'Kalburagi'}


max_key_length = max(len(str(key)) for key in sample_dict.keys())
max_value_length = max(len(str(value)) for value in sample_dict.values())


header = f'{"Key".ljust(max_key_length)} | {"Value".ljust(max_value_length)}'
separator = '-' * (max_key_length + 3 + max_value_length)


print(header)
print(separator)


for key, value in sample_dict.items():
    print(f'{str(key).ljust(max_key_length)} | {str(value).ljust(max_value_length)}')

