n = int(input())
crt = 0
li = []
for i in range(n,0,-1):
    a,b,c = map(int, str(i).zfill(3))
    
    crt = i + a + b + c
    if crt == n:
        li.append(i)        
        
if len(li) > 0: 
    print(min(li))
else:
    print(0)
