import sys

primary_list = [False, False]+[True]*9999

for i in range(2, 10000+1):
    if primary_list[i]:
        for j in range(2*i, 10000+1, i):
            primary_list[j] = False

T = int(sys.stdin.readline())
answer = []
for i in range(T):
    test_case = int(sys.stdin.readline())
    for i in range(test_case // 2 , test_case):
        if primary_list[i] and primary_list[test_case - i]:
            answer.append([test_case - i, i])
            break

for i in answer:
    print(i[0], i[1])



# import sys
#
# def P(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 return False
#         return True
#
# T = int(sys.stdin.readline())
# test_case = []
#
# for i in range(T):
#     test_case.append(int(sys.stdin.readline()))
#
# for t in test_case:
#     tmp_list = []
#     for i in range(2, t):
#         if P(i) == P(t-i) == True and i <= t - i:
#             tmp_list.append([i, t - i])
#     if len(tmp_list) == 1:
#         print(tmp_list[0][0], tmp_list[0][1])
#     else:
#         tmp_list.sort(key = lambda x: x[0], reverse=True)
#         print(tmp_list[0][0], tmp_list[0][1])