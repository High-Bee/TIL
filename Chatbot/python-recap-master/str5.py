nb = list(map(str, input().upper()))
n = 0
# for i in nb:
#     if ord(i) <= 67:
#         n += 3
#     elif ord(i) <= 70 and ord(i) > 67: 
#         n += 4
#     elif ord(i) <= 73 and ord(i) > 70: 
#         n += 5
#     elif ord(i) <= 76 and ord(i) > 73: 
#         n += 6
#     elif ord(i) <= 79 and ord(i) > 76: 
#         n += 7
#     elif ord(i) <= 83 and ord(i) > 79: 
#         n += 8
#     elif ord(i) <= 86 and ord(i) > 83: 
#         n += 9
#     elif ord(i) <= 90 and ord(i) > 86:
#         n += 10
    

print(n)

for i in nb:
    if i in "ABC":
        n += 3
    elif i in "DEF":
        n += 4
    elif i in "GHI":
        n += 5
    elif i in "JKL":
        n += 6
    elif i in "MNO":
        n += 7
    elif i in "PQRS":
        n += 8
    elif i in "TUV":
        n += 9
    elif i in "WXYZ":
        n += 10
print(n)    

    
    
    
    