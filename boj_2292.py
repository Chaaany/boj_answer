import sys

def p(n):
    return 6*n

N = int(sys.stdin.readline())
a = 1
answer = 1

while N > a:
    a+= p(answer)
    answer+= 1

print(answer)