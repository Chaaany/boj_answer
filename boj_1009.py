import sys

N = int(sys.stdin.readline())
answer = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
test_case = []

for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    test_case.append(a)

for case in test_case:
    if len(answer[case[0] % 10]) == 1:
        print(answer[case[0] % 10][0])
    else:
        print(answer[case[0] % 10][(case[1] % len(answer[case[0] % 10])-1)])
