import sys

N = int(sys.stdin.readline())
case = []
for i in range(N):
    case.append(int(sys.stdin.readline()))

case.sort()
for i in case:
    print(i)