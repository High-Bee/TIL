# # k = [[1,2],[3,1],[3,5]]

# # t = [sum(i) for i in k]

# # print(t)

# while True:
    
#     try:
#         a = list(map(int, input().split()))
#         print(sum(a))

#     except EOFError:
#         break
    
import sys
t = int(input())
s = [sys.stdin.readline().split() for i in range(t)]

print(s)
for i in s:
    k = list(map(str, i[1]))
    t = []
    n = ""
    for j in k:
        t = j*int(i[0])
        n += t
    print(n)


