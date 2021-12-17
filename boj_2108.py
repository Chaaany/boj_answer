import sys

N = int(sys.stdin.readline())
case_list = []
total = 0
counter = {}
for i in range(N):
    case_list.append(int(sys.stdin.readline()))
    total += case_list[i]


for i in case_list:
    if i in counter.keys():
        counter[i] += 1
    else:
        counter[i] = 1
print(counter)
max_counting_value = list(sorted(counter.items(), key=lambda x: x[1], reverse=True))[0][1]
print(max_counting_value)
max_counter = {k: v for k, v in counter.items() if v == max_counting_value}
max_counter = sorted(max_counter.items(), key=lambda x: x[0], reverse=False)
center_counter = sorted(list(set(list(counter))), reverse=True)
center_counter = center_counter[len(center_counter)//2]

print('{:.0f}'.format(total/N))
print(center_counter)
if len(counter) != 1:
    print(list(max_counter)[1][0])
else:
    print(list(max_counter)[0][0])
print(max(case_list) - min(case_list))
