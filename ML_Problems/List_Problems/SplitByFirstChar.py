def split_list_by_first_character(word_list):
    result_dict = {}

    for word in word_list:
        first_char = word[0]
        if first_char in result_dict:
            result_dict[first_char].append(word)
        else:
            result_dict[first_char] = [word]

    
    result_lists = list(result_dict.values())

    return result_lists


word_list = ['apple', 'banana', 'cherry', 'avocado', 'blueberry', 'blackberry']

split_lists = split_list_by_first_character(word_list)
print("Split lists based on first character:")
for lst in split_lists:
    print(lst)
