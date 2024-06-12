s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s1.difference(s2)

s3 = s1 - s2


print("it will return only the value not present in s2 set",s)
print("it will return only the value not present in s2 set using difference operator",s3)


print("=====*******========*******=======*******=========**********=========")



s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s = s2.difference(s1)
s4 = s2 - s1

print("it will return only the value not present in s1 set",s)
print("it will return only the value not present in s2 set using difference operator",s4)
