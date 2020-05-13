# 사칙연산 어떤순회인지 알아보기 같은거

def inorder(node):
    if node:
        inorder(tree[node][2])
        formula.append(tree[node][1])
        inorder(tree[node][3])
        # print(formula)


for tc in range(1):
    n = int(input())
    tree = [[0 for _ in range(4)] for _ in range(n+1)]
    for line in range(n):
        tmp = list(input().split())
        index = int(tmp[0])
        tree[index][0] = index
        if len(tmp)>=3:
            tree[index][2] = int(tmp[2])
        if len(tmp) == 4:
            tree[index][3] = int(tmp[3])
        tree[index][1] = tmp[1]
    formula = []
    inorder(1)
    result = 1
    print(formula)
    for i in range(len(formula)):
        if not i%2:
            if formula[i].isdigit() == False:
                result = 0
                break
        else:
            if formula[i] not in ['-', '+', '*', '/']:
                result = 0
                break
    print(f"#{tc + 1} {result}")