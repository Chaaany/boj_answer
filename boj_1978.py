import sys

def P(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

N = int(sys.stdin.readline())
test_case = list(map(int, sys.stdin.readline().split()))
count = 0

for test in test_case:
    if P(test):
        count += 1
print(count)

# 소수의 특징 - 2를 제외한 소수는 모두 홀수이다.
# 특정한 수가 그 수의 제곱근까지의 수로 나눠지지 않으면 그 수는 소수이다.






