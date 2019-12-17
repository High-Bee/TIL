import sys
n = int(input())
result = [list(map(str, sys.stdin.readline())) for i in range(n)]
for i in result:
    t = list(map(str, i))
    n = 0
    k = 0
    for j in t:
        if j == "O":
            k += 1
        else:
            k = 0
        n += k
    print(n)
        

# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX