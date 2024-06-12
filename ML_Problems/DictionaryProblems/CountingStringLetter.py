def count_letters_in_string(s):
    letter_count = {}

    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


sample_string = 'anand'


letter_count_dict = count_letters_in_string(sample_string)


print("Letter count dictionary:", letter_count_dict)
