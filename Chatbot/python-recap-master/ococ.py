p = input()
p = list(p)
print(p)
addList = []
for i in p:
    if i == '(':
        addList.append(p.pop(0))
    elif i == ')':
        if addList[-1] == '(':
            addList.append(p.pop(0))
    print(addList)
    print(p)