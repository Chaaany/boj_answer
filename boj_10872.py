import sys

def f(a):
    tmp=1
    if a == 0:
        return tmp
    else:
        for i in range(1, a+1):
            tmp *= i
    return tmp

N = int(sys.stdin.readline())

print(f(N))

# def factorial(n):
#     result = 1
#     if n > 0 :
#         result = n * factorial(n-1)
#     return result
#
# n = int(input())
# print(factorial(n))