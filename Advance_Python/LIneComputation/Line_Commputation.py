import math

print("welcome to line comparison computation")

def calculate_line_length(x1, y1, x2, y2):
    length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return length


x1, y1 = 3, 4
x2, y2 = 7, 1
length = calculate_line_length(x1, y1, x2, y2)
print(f"The length of the line segment is: {length}")
