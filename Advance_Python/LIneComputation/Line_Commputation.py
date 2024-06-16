import math

print("welcome to line comparison computation")

def calculate_length(x1, y1, x2, y2):
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def are_lines_equal(x1, y1, x2, y2, x3, y3, x4, y4):
  
    
    length1 = calculate_length(x1, y1, x2, y2)
    length2 = calculate_length(x3, y3, x4, y4)
    
  
    return length1 == length2

x1, y1, x2, y2 = 3, 4, 7, 1  
x3, y3, x4, y4 = 3, 4, 7, 1  
x5, y5, x6, y6 = 7, 1, 3, 4  
x7, y7, x8, y8 = 2, 3, 6, 5  

# Check equality
print(are_lines_equal(x1, y1, x2, y2, x3, y3, x4, y4))  
print(are_lines_equal(x1, y1, x2, y2, x5, y5, x6, y6))  
print(are_lines_equal(x1, y1, x2, y2, x7, y7, x8, y8))  
