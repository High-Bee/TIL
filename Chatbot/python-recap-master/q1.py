h,w,n = map(int, input().split())
k = 0
i = 1
j = 1
for i in range(w+1):
    i = str(i).zfill(2)
    
    for j in range(h+1):
        j = str(j)
        k= j+i
        print(k)