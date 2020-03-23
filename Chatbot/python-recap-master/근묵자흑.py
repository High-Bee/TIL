# n, k = map(int, input().split())
# tmp = list(map(int, input().split()))

# i = 0
# while len(set(tmp))==1:
# for i in range(len(tmp)):


# print(tmp)

# tmp.index(min(tmp))

# 4 3
# 2 3 1 4
# # 2

# 8 3
# 7 3 1 8 4 6 2 5
# # 4

# 37 4
# 31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
# # 12

# print(37%4)
N = int(input())

result = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    if i == 1:
        result[i] = 0
        continue
    result[i] = result[i-1] + 1
    if i % 3 == 0 and result[i//3] + 1 < result[i]:
        result[i] = result[i//3] + 1
    if i % 2 == 0 and result[i//2] + 1< result[i]:
        result[i] = result[i//2] + 1
        
print(result[N])
print(result)