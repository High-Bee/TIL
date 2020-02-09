# n=[1,2,3,4]

# print(1<<6)

# print(2**6)

def Bitprint(i):
    for j in range(7,-1,-1):
        print('1' if (i & (1<<j)) else'0', end='')

for i in range(-5,6):
    print('%2d = '%i, end='')
    Bitprint(i)
    print()

print()

a = 0b47FE
x = 0x01020304

print('%d ='%a, end='')
Bitprint(a)
print()

print('%08x ='%x,end='')
for i in range(0,25,8):
    Bitprint(x>>i)
    print(end=' ')

print()

n = 0x00111111
if n & 0x11:
    print('little endian',n)
else:
    print('big endian')

print()

a = 0x86
key = 0xAA

print('a ==>',end='')
Bitprint(a)
print()

print('a^=key ==>',end='')
a ^= key
Bitprint(a)
print()

print('a^=key ==>',end='')
a ^= key
Bitprint(a)
print()

print([0]*10)