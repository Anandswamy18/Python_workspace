def compute_harmonic_number(N):
    # Ensure N is not zero
    if N == 0:
        raise ValueError("N must be a non-zero integer.")
    
    harmonic_sum = 0.0
    for i in range(1, N + 1):
        harmonic_sum += 1 / i
    
    return harmonic_sum

N = int(input("Enter a positive integer N (N != 0): "))


if N == 0:
    print("N must be a non-zero integer.")
else:
   
    harmonic_number = compute_harmonic_number(N)
    print(f"The {N}th harmonic number is: {harmonic_number}")
