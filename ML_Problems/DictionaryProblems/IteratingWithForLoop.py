sample_dict = {'apple': 20, 'banana': 10, 'orange': 30, 'grape': 5}


print("Iterating over keys:")
for key in sample_dict:
    print(key)


print("Iterating over values:")
for value in sample_dict.values():
    print(value)


print("Iterating over key-value pairs:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")
