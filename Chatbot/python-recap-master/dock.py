t = int(input())

for i in range(1, t+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = sorted(a, key= lambda x: (x[1], x[0]))
    j = 0
    while j<(len(b)-1):
        
        if b[j][1] <= b[j+1][0]:
            j += 1
        elif b[j][1] >= b[j+1][0]:
            b.pop(j+1)
        elif b[j][1] == b[j+1][0]:
            b.pop(j+1)
        
    print(f'#{i} {len(b)}')