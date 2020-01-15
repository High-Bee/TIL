# n = int(input())
# crt = 0
# li = []
# for i in range(n,0,-1):
#     a,b,c = map(int, str(i).zfill(3))
    
#     crt = i + a + b + c
#     if crt == n:
#         li.append(i)        
#     elif i == 1:
#         print(0)
#     else:
#         print(min(li))

n = int(input())

res = 0
for i in range(n):
    a = sum(map(int, str(i)))
    crt = i + a
    if crt == n:
        res = i
        break       
print(res)
