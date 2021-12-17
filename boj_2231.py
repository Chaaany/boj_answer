import sys

for i in range(1,1000):
    N = i
    answer_list = []

    for i in range(1, N+1):
        M = i
        for j in str(i):
            M += int(j)
        if N == M:
           answer_list.append(i)

    if not answer_list:
        print(0)
    else:
        print(answer_list)

# N=int(input())
# r=0
# for i in range(max(0, N-41), N):
#  if sum(map(int,list(str(i))))+i==N:r=i;break
# print(r, N - r)
