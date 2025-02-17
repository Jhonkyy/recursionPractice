def Factorial(n):
    if n == 0:
        return 0
    else:
        return n * Factorial(n-1)
print(Factorial(5))