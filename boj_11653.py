import sys

def d(n):
    if n == 1:
        return
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            print(i)
            return d(n // i)
    print(n)

N = int(sys.stdin.readline())
d(N)






