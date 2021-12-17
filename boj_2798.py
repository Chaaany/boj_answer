import sys

N, M = map(int,sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))

sum = 0
answer = [0, 0, 0]

for a in card_list:
    for b in card_list:
        for c in card_list:
            if M - (a + b + c) <= M - sum and M - (a + b + c) >= 0 and a != b and b!=c and a!=c:
                sum = a + b + c
                answer = [a, b, c]

print(sum)