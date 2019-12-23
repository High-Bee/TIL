n = int(input())
words_ch = [input() for i in range(n)]
for i in words_ch:
    t = list(map(str, i))
    k = set(t)
    for j in t:
        
        print(t.index(j))