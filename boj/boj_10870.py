def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = Fibonacci(n-1) + Fibonacci(n-2)
    return result

N = int(input())
print(Fibonacci(N))