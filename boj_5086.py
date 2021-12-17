import sys

test_case = []
case = list(map(int,sys.stdin.readline().split()))

while case[0] != 0 and case[1] != 0:
    test_case.append(case)
    case = list(map(int, sys.stdin.readline().split()))

for case in test_case:
    if case[1] % case[0] == 0:
        print('factor')
    elif case[0] % case[1] == 0:
        print('multiple')
    else:
        print('neither')