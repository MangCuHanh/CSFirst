from os import system
import sys;
system('cls')
''
# import random
# for number in range(1, 1001):
#     print(number)
# so = a[0]
# j = a[0]
# for b in a:
#     if b > so:
#         so = b
#     if j > b :
#         j = b
# print(f"số lớn nhất là:{so}")
# print(f"số nhỏ nhất là:{j}")
# print(f"số lớn nhất là:{max(a)}")
# print(f"số nhỏ nhất là:{min(a )}")
a = [1,2,3,4,5,6,7,8,9,0,425]
d = []
c = []
for b in a:
    if b % 2 == 0:
        c.append(b)         
    else:
        d.append(b)
print(f"danh sách số lẻ là:{d}")
print(f"danh sách số chẳn là:{c}")



