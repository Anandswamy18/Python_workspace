import math

def calculate_length(x1, y1, x2, y2):
   
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def compare_lines(x1, y1, x2, y2, x3, y3, x4, y4):
    
    length1 = calculate_length(x1, y1, x2, y2)
    length2 = calculate_length(x3, y3, x4, y4)
    
    if length1 < length2:
        return "third line is shorter"
    elif length1 > length2:
        return "first line is longer"
    else:
        return "lines are equal"

x1, y1, x2, y2 = 3, 4, 7, 1 
x3, y3, x4, y4 = 3, 4, 7, 1  
x5, y5, x6, y6 = 2, 3, 6, 5 


print(compare_lines(x1, y1, x2, y2, x3, y3, x4, y4))  
print(compare_lines(x1, y1, x2, y2, x5, y5, x6, y6))  
print(compare_lines(x5, y5, x6, y6, x1, y1, x2, y2))  
