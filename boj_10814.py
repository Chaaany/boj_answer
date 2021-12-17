import sys

N = int(sys.stdin.readline())
registration_list = []

for i in range(N):
    registration_list.append(list(sys.stdin.readline().split()))
    registration_list[i].append(i)

registration_list = sorted(registration_list, key = lambda x: (int(x[0]), int(x[2])))

for person in registration_list:
    print(int(person[0]), person[1])