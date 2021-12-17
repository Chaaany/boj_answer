import sys

N = sys.stdin.readline().strip()
descending_list = [i for i in N]
descending_list=sorted(descending_list, reverse=True)
answer = ""

for n in descending_list:
    answer+=n

print(int(answer))

