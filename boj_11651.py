import sys

N = int(sys.stdin.readline())
point_list = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    point_list.append([y, x])

point_list = sorted(point_list, key = lambda x: (x[0], x[1]))

for point in point_list:
    print(point[1], point[0])