t = int(input())
c = 0
for i in range(1, t+1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    for j in w:
        for k in t:
            if k >= j:
                c+=j
            
        print(c)