import sys
import math
info = list(map(int,sys.stdin.readline().split()))

fixed_cost = info[0]
variable_profit = info[2] - info[1]

if variable_profit > 0:
    if fixed_cost % variable_profit != 0:
        print(math.ceil(fixed_cost / variable_profit))
    else:
        print( int(fixed_cost / variable_profit + 1))
else:
    print(-1)


