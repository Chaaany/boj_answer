import sys


Test = int(sys.stdin.readline())
test_case = []
#Test case 받기
for i in range(Test):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    test_case.append([k,n])

def S(k, n):
    model = []
    for i in range(k+1):
        line = []
        for j in range(n):
            line.append(0)  # 안쪽 리스트에 0 추가
        model.append(line)  # 전체 리스트에 안쪽 리스트를 추가
    for floor in range(k+1):
        for room in range(n):
            if floor == 0:
                model[floor][room] = room + 1
            elif room == 0:
                model[floor][room] = 1
            else:
                model[floor][room] = model[floor-1][room] + model[floor][room-1]

    return model[k][n-1]


for i in range(Test):
    print(S(test_case[i][0], test_case[i][1]))


#
# 1, 3 = [0, 3] + [1, 2]
# [k, n] = [k-1, n] + [k, n-1]






#
# for test_count in range(Test):
#     a = int(sys.stdin.readline())
#     b = int(sys.stdin.readline())
#
#     tmp_list_1 = []
#     tmp_list_1.append(S(b))
#     print(tmp_list_1)
#     for i in range(1, b+1):
#         tmp_list_2 = [1]
#         for j in range(a):
#             tmp_list_2.append(tmp_list_1[i-1][j]+tmp_list_2[j-1])
#         print(tmp_list_2)
#         tmp_list_1.append(tmp_list_2)
#         print(tmp_list_1)
#     # print(tmp_list_1[b][a])
#
#
# #
# #     for
# #
# #
# # print(answer)
#

    # test[k][n] = test[k][n-1] + test[k-1][n]
