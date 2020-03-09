n, k = map(int,input().split())
a = [int(input()) for _ in range(n)]
b = 0

for i in reversed(a):
    if k >= i:
        b += k//i
        k = k - ((k//i)*i)  
    if k == 0:
        break
                
print(b)

  
