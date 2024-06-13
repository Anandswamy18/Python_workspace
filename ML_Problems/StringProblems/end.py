def modify_string(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'


sample_string1 = 'abc'
sample_string2 = 'string'


print(f"Original String: {sample_string1} => Modified String: {modify_string(sample_string1)}")
print(f"Original String: {sample_string2} => Modified String: {modify_string(sample_string2)}")
