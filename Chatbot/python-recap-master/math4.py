x = int(input())

i = 0

while x > 0:
    x -= i
    i += 1
    print(x, i)

x = i+x-1
res = str(x)+"/"+str(i-x)

if i % 2 == 0:
    res = str(i-x) +"/"+ str(x)
print(res)
