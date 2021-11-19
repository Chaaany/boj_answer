import sys

def F(x, y):
    distance = y - x
    i = 1
    while True:
        if i % 2 == 0:
            if (i // 2) ** 2 < distance <= (i // 2) * (i // 2 + 1):
                return i
        if i % 2 != 0:
            if (i // 2) * (i // 2 + 1) < distance <= (i // 2 + 1) ** 2:
                return i
        i += 1

N = int(sys.stdin.readline())
test_case = []

for i in range(N):
    test_case.append(list(map(int, sys.stdin.readline().split())))

for test in test_case:
    print(F(test[0], test[1]))
