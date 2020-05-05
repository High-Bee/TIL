import math
n, m = map(int, input().split())
tmp = list(map(int, input().split()))
l = n - m
if l > 0:
    k = math.ceil(l/(m-1))
    k = k+1
print(k)


