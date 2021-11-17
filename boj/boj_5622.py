import sys

number = sys.stdin.readline().strip()
dials = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ", "0"]

time = 0

for i in number:
    for dial in dials:
        if i in dial:
            time = (time + dials.index(dial)+2)

print(time)


