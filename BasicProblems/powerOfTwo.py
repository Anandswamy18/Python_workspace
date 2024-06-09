def print_powers_of_2(N):
   
    if N < 0 or N >= 31:
        print("N must be between 0 and 30 (inclusive).")
        return
    
    
    for i in range(N + 1):
        print(f"2^{i} = {2 ** i}")


try:
    N = int(input("Enter the power value N (0 <= N < 31): "))
    print_powers_of_2(N)
except ValueError:
    print("Please enter a valid integer.")
