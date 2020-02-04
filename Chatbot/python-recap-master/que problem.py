s=[]
def push(x):

    s.append(x)

def pop():
    if len(s)==0:
         return -1
    else:
        s.pop()

def size():
    return len(s)

def empty():
    if len(s)==0:
        return 1
    else:
        return 0
def front():
    if len(s)==0:
        return -1
    else:
        return s[0]

def back():
    if not len(s):
        return -1
    else:
        s[-1]

T = int(input())
for tc in range(1,T+1):
    inp = list(input().split())
    # print(f"{inp[0](int(inp[1]))}")
    if inp[0] == "push":
        push(inp[1])
    if inp[0] == "front":
        print(front())
