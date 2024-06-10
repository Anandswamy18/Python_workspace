def prime_factors(N):
    
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    
    factors = []
    
    i = 2
    
    while i * i <= N:
        
        while (N % i) == 0:
            factors.append(i)
            N =N/ i
        i += 1
    
  
    if N > 1:
        factors.append(N)
    
    return factors


N = int(input("Enter a positive integer N: "))


if N <= 0:
    print("N must be a positive integer.")
else:
   
    factors = prime_factors(N)
    print(f"The prime factors of {N} are: {factors}")
