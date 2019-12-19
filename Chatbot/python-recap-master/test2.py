# a = int(input())

# t = list(map(int,str(a)))
# while True:
#     str

#     if sum(t) == a:
#         break
# 수학의 나머지 자릿수로 %10 계산해야 정답이 풀린다
n =int(input())
a = 0
i = 0
t = 0
if n < 10:
    n = int(str(n)+"0")
k = n
while True:
    if k != a:
        t = n//10 + n%10
        a = n%10
        n = a
        i += 1
        
    else:
        print(i)
        break


# n = 26
# k = n%10
# t = sum(map(int,str(n)))
# s = int(str(k)+str(t))
# n = int(str(k)+str(t))
# t = str(sum(map(int,str(n))))[-1]