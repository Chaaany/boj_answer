import sys

N = int(sys.stdin.readline())
test_case = list(map(int, sys.stdin.readline().split()))

test_case.sort(reverse=False)
time = 0

for i in range(1, N+1):
    time += test_case[i-1] * (N-i+1)

print(time)

