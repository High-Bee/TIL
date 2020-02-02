T = int(input())
s = []

for tc in range(1, T+1):
    sentence = list(map(str, input()))
    s= []
    for i in sentence:
        if i in "({":
            s.append(i)
        elif i in "})":
            if len(s) == 0:
                s.append(i)
                break
            elif (i == ")" and s[-1] != "(") or (i == "}" and s[-1] != "{"):
                s.append(i)
                break
            else:
                s.pop()

    if not len(s):
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")