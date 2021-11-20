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
# tmp_case = int(sys.stdin.readline())
# test_list = []
# while tmp_case:
#     test_list.append(tmp_case)
#     tmp_case = int(sys.stdin.readline())
#
# for test in test_list:
#     count = 0
#     if test == 1:
#         print(1)
#     elif test % 2:
#         for i in range(test+2, 2 * test, 2):
#             if P(i):
#                 count += 1
#         print(count)
#     else:
#         for i in range(test+1, 2 * test, 2):
#             if P(i):
#                 count += 1
#         print(count)
import sys

primary_list = [False, False]+[True]*(123456*2-1)

for i in range(2, int((123456*2)**0.5)+1):
    if primary_list[i]:
        for j in range(2*i, 123456*2+1, i):
            primary_list[j] = False

tmp_case = int(sys.stdin.readline())
test_list = []
while tmp_case:
    test_list.append(tmp_case)
    tmp_case = int(sys.stdin.readline())

for test in test_list:
    print(primary_list[test+1:2*test+1].count(True))

