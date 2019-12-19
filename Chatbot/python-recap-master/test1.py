# k = [[1,2],[3,1],[3,5]]

# t = [sum(i) for i in k]

# print(t)

while True:
    
    try:
        a = list(map(int, input().split()))
        print(sum(a))

    except EOFError:
        break
    