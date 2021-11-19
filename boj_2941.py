import sys

Croatian_word = input()
conversion_alphabet_two = ["c=", "s=", "z=", "c-", "d-", "lj", "nj"]
conversion_alphabet_three = "dz="

word_length = len(Croatian_word)


for i in conversion_alphabet_two:
    if i in Croatian_word:
        word_length = (word_length - Croatian_word.count(i))


if conversion_alphabet_three in Croatian_word:
    word_length = (word_length - Croatian_word.count(conversion_alphabet_three))

print(word_length)
