n = int(input())
m = int(input())

ad = [[] for _ in range(n+1)]
for _ in range(1, m+1):
    e1, e2 = map(int, input().split())
    ad[e1].append(e2)
    ad[e2].append(e1)
    print(ad)