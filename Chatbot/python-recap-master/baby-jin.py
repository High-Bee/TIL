t = int(input())

for i in range(1,t+1):
    a = list(map(int, input().split()))
    p1 = [[]for _ in range(10)]
    p2 = [[]for _ in range(10)]
    p1_t = 0
    p2_t = 0
    # k = 0
    for j in range(len(a)):
        if j % 2 == 0:
            p1[a[j]].append(a[j])
        if j % 2 != 0:
            p2[a[j]].append(a[j])

    # while k < len(p1):
    for k in range(len(p1)):
        p1_t += 1
        p2_t += 1

        if len(p1[k]) == 0:
            p1_t = 0
        if len(p1[k]) == 3 or (p1_t == 3):
            print(f'#{i} {1}')
            break

        if len(p2[k]) == 0:
            p2_t = 0        
        if len(p2[k]) == 3 or (p2_t == 3):
            print(f'#{i} {2}')
            break
        if k == len(p1)-1:
            print(f'#{i} {0}')
            break
        # k += 1