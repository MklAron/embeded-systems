import time

def factorize(n):
    factors = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorization_time(n):
    start_time = time.time()
    factors = factorize(n)
    end_time = time.time()
    print(f"Factors of {n}: {factors}")
    print(f"“Elapsed time: {end_time - start_time:.6f} seconds")
n = int(input("Enter a number to factorize: "))
factorization_time(n)
