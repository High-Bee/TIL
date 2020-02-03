# '''
# 문제 2.
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# '''

# numbers = int(input('숫자를 입력하세요: '))

# for i in range(1,numbers+1):
#     print(i)
x = [30,10,10]
print(x.count(30))

x_ = []
y_ = []
for i in range(3):
        x, y = map(int, input().split())
        x_.append(x)
        y_.append(y)
for i in range(3):
        if x_.count(x_[i]) == 1:
                x = x_[i]
        if y_.count(y_[i]) == 1:
                y = y_[i]
print(x, y)