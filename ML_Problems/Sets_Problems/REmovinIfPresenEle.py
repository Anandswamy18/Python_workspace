def check_element_and_remove(ele):
    my_Set = {8, 4, 6, 54}
    print("before discarding element:", ele)
    for i in my_Set.copy():  
        if i == ele:
            my_Set.discard(ele)
            print("After discarding element:", ele, my_Set)
            return  

   
    print("The element is not present")


element = int(input("Enter a number to remove from the set: "))
check_element_and_remove(element)
