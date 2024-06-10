def is_perfect_number(N):
   
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    
   
    sum_of_divisors = 0
    
    
    for i in range(1, N):
        if N % i == 0:
            sum_of_divisors += i
    
   
    return sum_of_divisors == N


N = int(input("Enter a positive integer N: "))


if N <= 0:
    print("N must be a positive integer.")
else:
  
    if is_perfect_number(N):
        print(f"{N} is a perfect number.")
    else:
        print(f"{N} is not a perfect number.")
