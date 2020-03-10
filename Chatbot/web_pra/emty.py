# arr = [2,3,4,5]
# bit = [0]*len(arr)

# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for q in range(2):
#                 bit[3] = q
#                 print([arr[x] for x in range(len(bit)) if bit[x]])

# arr = [2,3,4,5]
# n = len(arr)

# for i in range(1<<n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=",")
#     print()
# n = 4
# for i in range(1<<n):
#     print(i)

import itertools as it
mylist = ['a','b','c','d','e']
result = it.combinations(mylist, r=3)

print(list(result))
print()
print(result)