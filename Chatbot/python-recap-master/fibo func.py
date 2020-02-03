# def fiboni(n):
#     if n < 2:
#         return n
#     else:
#         return fiboni(n-1)+fiboni(n-2)


# # fiboni(10)
## 계산 중복이 엄청남

# memo = [0,0]
def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1)+fibo(n-2))
    return memo[n]

memo = [0,1]
# 계산중복을 없엔 알고리즘(Memoization)

print(fibo(500))


