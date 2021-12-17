import sys

N = int(sys.stdin.readline())
word_list = []

for i in range(N):
    word_list.append(sys.stdin.readline().strip())
word_list = list(set(word_list))

for i in range(len(word_list)):
     word_list[i] = [word_list[i], len(word_list[i])]

# word_list = sorted(word_list, key = lambda x: (len(x[0]), x[0]))
word_list = sorted(word_list, key = lambda x: (x[1], x[0]))

for word in word_list:
    print(word[0])
