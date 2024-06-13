def get_last_part_of_string(string, delimiter):
    
    last_index = string.rfind(delimiter)
    
   
    if last_index != -1:
        
        result = string[:last_index]
        return result
    else:
       
        return string


url1 = "https://www.w3resource.com/python-exercises"
url2 = "https://www.w3resource.com/python"

print(get_last_part_of_string(url1, '/'))   
print(get_last_part_of_string(url2, '/'))   
