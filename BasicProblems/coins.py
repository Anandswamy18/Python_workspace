import random

def flip_coin(num_flips):
    if num_flips <= 0:
        print("Number of flips must be a positive integer.")
        return
    
    heads_count = 0
    tails_count = 0
    
    for _ in range(num_flips):
        if random.random() < 0.5:
            tails_count += 1
        else:
            heads_count += 1
    
    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100
    
    print(f"Heads: {heads_percentage:.2f}%")
    print(f"Tails: {tails_percentage:.2f}%")


num_flips = int(input("Enter the number of times to flip the coin: "))
flip_coin(num_flips);
