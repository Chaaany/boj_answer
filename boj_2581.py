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

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
numberlist = []
min_value = 0
total = 0

for test in range(M, N + 1):
    if P(test):
        total += test
        numberlist.append(test)
if not numberlist:
    print(-1)
else:
    print(f'{total}\n{numberlist[0]}')
