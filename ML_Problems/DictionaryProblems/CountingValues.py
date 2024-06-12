def count_success_true(data):
    count = 0

    for item in data:
        if item.get('id') == True:
            count += 1
    return count


sample_data = [
    {'id': 1, 'success': True, 'name': 'swamy'},
    {'id': 2, 'success': False, 'name': 'REavi'},
    {'id': 3, 'success': True, 'name': 'Virat'},
    {'id': 3, 'success': True, 'name': 'sujan'}
]


result = count_success_true(sample_data)

print("Count of dictionaries with 'success' as True:", result)
