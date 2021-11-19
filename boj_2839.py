
N = int(input())
answer = []

for x in range(1001):
    for y in range(1668):
        if N == (5 * x + 3 * y):
            answer.append([x, y])

if len(answer) == 0:
    print(-1)

else:
    print(answer)
    min_list = max(answer)
    print(min_list[0]+ min_list[1])

