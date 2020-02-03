# 3

# XYPV
# EOGGXYPVSY
# STJJ
# HOFSTJPVPP
# ZYJZXZTIBSDG
# TTXGZYJZXZTIBSDGWQLW

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    n, q = 0, 0
    for i in str1:
        for j in str2:
            if i == j:
                n += 1
        if n > q:
            q = n
        n = 0
    print(f"#{tc} {q}")