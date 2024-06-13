def find_long_words(word_list, n):
    
    long_words = []

   
    for word in word_list:
       
        if len(word) > n:
            
            long_words.append(word)

 
    return long_words


words = ["apple", "banana", "cherry", "date", "fig", "grape"]
n = int(input("Enter the length n: "))


result = find_long_words(words, n)



print(f"Words longer than {n} characters:", result)
