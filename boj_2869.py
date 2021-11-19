import sys
import math

snail = list(map(int, sys.stdin.readline().split()))

print(math.ceil((snail[2] - snail[1]) / (snail[0] - snail[1])))
