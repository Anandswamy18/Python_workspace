def lowercase_first_n(s, n):
    if n <= len(s):
        return s[:n].lower() + s[n:]
    else:
        return s.lower()


input_string = "HelloWorld"
n = 5
result = lowercase_first_n(input_string, n)
print(f"After lowering first {n} characters: {result}")
