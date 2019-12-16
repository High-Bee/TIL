import sys
a = [int(sys.stdin.readline()) for i in range(10)]
t = []
for i in a:
    t.append(i % 42)

t = set(t)
print(len(t))    
