import sys

N = int(sys.stdin.readline())
case = []
tmp_list = []
for i in range(N):
   tmp_list = list(map(int, sys.stdin.readline().split()))
   case.append(tmp_list + [1])


for a in range(len(case)):
   for b in range(len(case)):
      if case[a][0] > case[b][0] and case[a][1] > case[b][1]:
         case[b][2] += 1

for i in case:
   print(i[2], end=" ")