# t = "sdfFSDFEWSDz"

# a = list(set(t.upper()))


# print(a)

words = input().lower()
words_list = list(set(words))
word_count = list()

print(words_list)
for i in words_list:
    count = words.count(i)
    word_count.append(count)

if(word_count.count(max(word_count)) >= 2):
    print('?')
else:
    print(words_list[(word_count.index(max(word_count)))].upper())