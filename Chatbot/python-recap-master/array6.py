import sys
n = int(input("과목수 : "))
score = list(map(int,sys.stdin.readline().split()))
t = []
for i in score:
    t.append((i/max(score))*100)

print(sum(t)/n)