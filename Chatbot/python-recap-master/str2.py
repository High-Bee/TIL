# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다. 
# sys 쓰니까 개행문자 입력으로 값 한개일 때 오류가 발생하더라 시발 열받으니까 개행문자처리하는거 잘 숙지하고 있자.
# 다른 문자열 처리 - 패턴은 익숙하지만 입출력 처리 또 줫같이 됐다. 1시간 안녕

a = input().upper()

p = list(set(a))
k = []
print(p)
for i in p:
    count = a.count(i)
    k.append(count)

if(k.count(max(k)) >= 2):
    print('?')
else:
    print(p[(k.index(max(k)))])




# i = 1
# for i in range(len(k)):
#     a.index(max(a.count(i)))
#####################################################
# a = "asDSFDSFSDAAaaaed"
# t = list(map(str, a.upper()))
# k = sorted(t)
# print(k)
# l = []
# c = ""
# q = []
# for i in k:
#     n = i
#     if n == i:
#         l = i
#     if l not in c:
#         c = ""
       
#     c += n
#     print(c)
#     print(q)