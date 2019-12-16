import sys
c = int(input())
result = [list(map(int, sys.stdin.readline().split())) for i in range(c)]
for i in result:
    t = (sum(i[1:])/i[0])
    n = 0
    for j in i[1:]:
        if j > t:
            n += 1
        k = (n/(len(i)-1)) * 100
    print("%.3f" %round(k,3)+"%")

