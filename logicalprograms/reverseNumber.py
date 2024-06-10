def reverse(num):
    reversed_num = 0

   
    while num != 0:
        digit = num % 10  
        reversed_num = reversed_num * 10 + digit  
        num = num // 10  

    return reversed_num


number = int(input("Enter a number to reverse: "))


reversed_number = reverse(number)

print("Original number:", number)
print("Reversed number:", reversed_number)
