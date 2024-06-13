def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


sample_string = "Anand"
result = count_characters(sample_string)
print("Character frequency in '{}' is: {}".format(sample_string, result))
