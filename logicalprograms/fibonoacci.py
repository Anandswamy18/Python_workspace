def generate_fibonacci(N):
   
    if N <= 0:
        raise ValueError("N must be a positive integer.")
    
   
    a = 0
    b = 1
    result = []
    
    for _ in range(N):
        result.append(a)
       
        next_term = a + b
       
        a = b
        b = next_term
    
    return result


N = int(input("Enter a positive integer N: "))


if N <= 0:
    print("N must be a positive integer.")
else:
   
    series = generate_fibonacci(N)
    print(f"The first {N} terms of the Fibonacci series are: {series}")
