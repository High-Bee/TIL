
# n = int(input())

# p= str(n-1)+"666"

# if p[0] == 6:
#     print(p)
# else:
#     print(k)
from tqdm import tqdm
N = int(input())
movie = 666

while N:
    if "666" in str(movie):
        N -= 1
    movie += 1
    print(N, movie)

print(movie - 1) 