# import sys
#
# T = int(input())
# test_case = []
# for i in range(T):
#     test_case.append(list(map(int, sys.stdin.readline().split())))
#
# for case in test_case:
#     points_distance = ((case[0] - case[3]) ** 2 + (case[1] - case[4]) ** 2) ** 0.5
#
#     if case[2] > case[5] and case[2] > points_distance:
#         if points_distance + case[5] < case[2]:
#             print(0, '1-1')
#         elif points_distance + case[5] == case[2]:
#             print(1, '1-2')
#         else:
#             print(2, '1-3')
#     elif case[2] > case[5] and case[2] == points_distance:
#         print(2, '2-1')
#     elif case[2] > case[5] and case[2] < points_distance:
#         if points_distance > case[2] + case[5]:
#             print(0,'3-1')
#         elif points_distance == case[2] + case[5]:
#             print(1, '3-2')
#         else:
#             print(2, '3-3')
#     elif case[2] < case[5] and case[5] > points_distance:
#         if points_distance + case[2] < case[5]:
#             print(0, '4-1')
#         elif points_distance + case[2] == case[5]:
#             print(1, '4-2')
#         else:
#             print(2, '4-3')
#     elif case[2] < case[5] and case[5] == points_distance:
#         print(2, '5-1')
#     elif case[2] < case[5] and case[5] < points_distance:
#         if points_distance > case[2] + case[5]:
#             print(case, points_distance)
#             print(0, '6-1')
#         elif points_distance == case[2] + case[5]:
#             print(1, '6-2')
#         else:
#             print(2, '6-3')
#     elif case[2] == case[5] and points_distance > case[2] + case[5]:
#         print(0, '7-1')
#     elif case[2] == case[5] and points_distance == case[2] + case[5]:
#         print(1, '8-1')
#     elif case[2] == case[5] and points_distance < case[2] + case[5]:
#         print(2, '9-1')
#     else:
#         print(-1, '10-1')
#

import sys

T = int(input())
test_case = []
for i in range(T):
    test_case.append(list(map(int, sys.stdin.readline().split())))

for case in test_case:
    points_distance = ((case[0] - case[3]) ** 2 + (case[1] - case[4]) ** 2) ** 0.5

    if case[2] > case[5] and case[2] > points_distance:
        if points_distance + case[5] < case[2]:
            print(0)
        elif points_distance + case[5] == case[2]:
            print(1)
        else:
            print(2)
    elif case[2] > case[5] and case[2] == points_distance:
        print(2)

    elif case[2] > case[5] and case[2] < points_distance:
        if points_distance > case[2] + case[5]:
            print(0)
        elif points_distance == case[2] + case[5]:
            print(1)
        else:
            print(2)
    elif case[2] < case[5] and case[5] > points_distance:
        if points_distance + case[2] < case[5]:
            print(0)
        elif points_distance + case[2] == case[5]:
            print(1)
        else:
            print(2)
    elif case[2] < case[5] and case[5] == points_distance:
        print(2)
    elif case[2] < case[5] and case[5] < points_distance:
        if points_distance > case[2] + case[5]:
            print(0)
        elif points_distance == case[2] + case[5]:
            print(1)
        else:
            print(2)
    elif case[2] == case[5] and points_distance > case[2] + case[5]:
        print(0)
    elif case[2] == case[5] and points_distance == case[2] + case[5]:
        print(1)
    elif case[2] == case[5] and points_distance < case[2] + case[5] and points_distance != 0:
        print(2)
    else:
        print(-1)