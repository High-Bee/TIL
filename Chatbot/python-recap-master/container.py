# 입력
# 3

# 3 2
# 1 5 3
# 8 3

# 5 10
# 2 12 13 11 18
# 17 4 7 20 3 9 7 9 20 5

# 10 12
# 10 13 14 6 19 11 5 20 11 14
# 5 18 17 8 9 17 18 4 1 16 15 13

t = int(input())


for i in range(1, t+1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    c = 0
    k = 0
    w.sort(reverse=True)
    t.sort(reverse=True)

    while len(t) > 0 and len(w) >0:      
        if t[0] >= w[0]:
            t.pop(0)
            c += w.pop(0)
         
        elif t[0] <= w[0]:
            w.pop(0)
        k += 1    
    print(f'#{i} {c}')


    # elif (len(t) != True) or (len(w) != True):
    #         break