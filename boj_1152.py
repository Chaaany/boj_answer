import sys

phrase = sys.stdin.readline().strip()

if phrase == "":
    print(0)
else:
    print(phrase.count(' ') + 1)