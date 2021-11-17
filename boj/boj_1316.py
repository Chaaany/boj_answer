import sys
from string import ascii_lowercase

N = int(input())
Word_list = []
Alphabet_lowercase = list(ascii_lowercase)
count = 0

for i in range(N):
    Word_list.append(sys.stdin.readline().strip())

for word in Word_list:
    tmp_count = True
    for alphabet_index in Alphabet_lowercase:
        if alphabet_index in word and word[word.index(alphabet_index):word.index(alphabet_index)+word.count(alphabet_index)].count(alphabet_index) != word.count(alphabet_index):
           tmp_count = False

    if tmp_count:
        count+= 1

print(count)



