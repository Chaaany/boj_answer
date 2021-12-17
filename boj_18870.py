import sys

N = int(sys.stdin.readline())
case_list = list(map(int, sys.stdin.readline().split()))
tmp_case = sorted(list(set(case_list)))

for i in range(N):
    print(tmp_case.index(case_list[i]), end=" ")
