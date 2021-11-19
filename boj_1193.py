import sys

def f(a):
    n = 0
    total = 0
    while total < a:
        n += 1
        total+= n
    if n % 2 == 0:
        return f"{a - (total - n)}/{n+1 - (a - (total - n))}"
    else:
        return f"{n + 1 - (a - (total - n))}/{a - (total - n)}"
X = int(sys.stdin.readline())

print(f(X))
