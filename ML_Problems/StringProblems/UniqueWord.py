def unique_sorted_words():
   
    words_input = input("Enter a comma-separated sequence of words: ")
    
  
    words_list = words_input.split(',')
    
    
    words_list = [word.strip().lower() for word in words_list]
    
   
    unique_words_set = set(words_list)
    
    
    sorted_unique_words = sorted(unique_words_set)
    
    
    print("Unique words in sorted order:", ", ".join(sorted_unique_words))


unique_sorted_words()
