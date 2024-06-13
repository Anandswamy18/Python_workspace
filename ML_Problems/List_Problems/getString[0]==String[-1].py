def count_special_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

sample_list = ['abc', 'xyx', 'aba', '1221']
result = count_special_strings(sample_list)
print("Expected Result:", result)
