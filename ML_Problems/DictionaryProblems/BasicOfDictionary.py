person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person['first_name'])
print(person['favorite_colors'])
print(person['active'])


print(person.get('first_name'))
print(person.get('favorite_colors'))


person['gender']='male'

print(person.get('gender'))
print(person)



print(person.items())



person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for key, value in person.items():
    print(f"{key}: {value}")



person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for key in person.keys():
    print(key)



person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

for value in person.values():
    print(value)    