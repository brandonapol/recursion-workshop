def factorial(n):
    if n < 2:
        return n
    print(f'factorial({n}) = {n} * facrotial({n-1})')
    return n * factorial(n-1)


