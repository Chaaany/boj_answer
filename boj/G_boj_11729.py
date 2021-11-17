import sys

#
# def Hanoi(n):
#     if n == 1:
#         print(1)
#         print("1 3")
#     else:
#         print(2**(n-1)-1)
#         stick = [[1, []], [2,[]], [3,[]]]
#         round_board = [a for a in range(n)]
#         stick[0][1] = round_board
#         print(stick)
#         for i in range(n-1):
#             stick[1][1].append(stick[0][1].pop(0))
#             print(stick[0][0], stick[1][0])
#         print(stick)
#         stick[1][1].sort()
#
#         stick[2][1].append(stick[0][1].pop(0))
#         print(stick[0][0], stick[2][0])
#
#         print(stick)
#         for i in range(n-1):
#             stick[2][1].append(stick[1][1].pop(0))
#             print(stick[1][0], stick[2][0])
#         stick[2][1].sort()
#         print(stick)
#
# N = int(sys.stdin.readline())
# Hanoi(N)


def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n - 1, start, 6 - start - end)  # 1단계
    print(start, end)  # 2단계
    hanoi_tower(n - 1, 6 - start - end, end)  # 3단계


n = int(input())
print(2 ** n - 1)
hanoi_tower(n, 1, 3)

'''
장대를 세 개 만듭니다. 1, 2, 3
원판을 생성합니다. 1,2,3,4,5,6,..., n개 순서대로

그 위의 원판들을 목적지(3번)가 아닌 부목적지(2번)으로 옮긴다.
`
제일 아래 원판을 목적지인 3번 장대로 옮긴다(제일 가운데 순서)

부목적지(2번)의 원판들을 목적지인 3번 장대로 옮긴다

크게 3단계로 분류합니다. 
원판 1 
1 3

원판 2
1 2 
---
1 3
--- 
2 3

원판 3
1 3
1 2
3 2
----
1 3
----
2 1
2 3
1 3

'''






