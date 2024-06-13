def longest_word_length(word_list):
    max_length = 0

    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)

    return max_length


words = ['apple', 'banana', 'grapefruit', 'orange', 'kiwi']
print("List of words:", words)
print("Length of the longest word:", longest_word_length(words))
