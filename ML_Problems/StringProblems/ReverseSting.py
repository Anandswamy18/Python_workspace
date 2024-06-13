def reverse_string(s):
    reversed_str = ""
    slength = len(s)
    for i in range(slength - 1, -1, -1):
        reversed_str += s[i]
    print(reversed_str)


reverse_string("anand")
