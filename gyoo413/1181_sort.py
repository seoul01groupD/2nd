n = int(input())
word_list = []
for i in range(n):
    word_list.append(input())

word_with_len = []
for i in range(n):
    word_with_len.append([word_list[i], len(word_list)])

