from itertools import permutations

def generate_permutations(input_list):
    
    perm = permutations(input_list)
    
   
    for p in perm:
        print(p)


input_list = [1, 2, 3]
print(f"Permutations of {input_list}:")
generate_permutations(input_list)
