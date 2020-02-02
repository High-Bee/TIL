T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
n = 0
for tc in range(1, T + 1):
    s = list(map(str, input()))
    while True:
 
        if s[n] == s[n+1]:
            s.pop(n)
            s.pop(n)
            n = 0
        elif s[n] != s[n+1]:
            n += 1
        
        if len(s) == n+1:
            break


    print(f"#{tc} {len(s)}")   



# s = ["s","v","D"]
# s.pop(1)
# s.pop(2)
# print(s)