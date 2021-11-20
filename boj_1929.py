import sys

def P(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

M = list(map(int, sys.stdin.readline().split()))
numberlist = []

for test in range(M[0], M[1]+1):
    if P(test):
        numberlist.append(test)

for i in numberlist:
    print(i)