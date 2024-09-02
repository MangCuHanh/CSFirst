from os import system
import sys;
system('cls')
''
hng1=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng2=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng3=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng4=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng5=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng6=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng7=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng8=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng9=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
hng0=["🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳","🌳"]
for cay in hng1:
    print(cay,end="")
print()
for cay in hng2:
    print(cay,end="")
print()
for cay in hng3:
    print(cay,end="")
print()
for cay in hng4:
    print(cay,end="")
print()
for cay in hng5:
    print(cay,end="")
print()
for cay in hng6:
    print(cay,end="")
print()
for cay in hng7:
    print(cay,end="")
print()
for cay in hng8:
    print(cay,end="")
print()
for cay in hng9:
    print(cay,end="")
print()
for cay in hng0:
    print(cay,end="")
print()
a = input("bạn muốn nơi bạn cất giấu kho báu ở toa độ nào?\n")
b=int(a[0])
c=int(a[2])
map = hng1,hng2,hng3,hng4,hng5,hng6,hng7,hng8,hng9,hng0

ha = ["✖️","❌","❓","🔴"]
add = int(input("bạn muốn chọn hình nào?:\nnhập 1 = ✖️\nnhập 2 = ❌\nnhập 3 = ❓\nnhập 4 = 🔴:\n"))
if add <= 4:
    hhh = map[b]
    hhh[c] = ha
    map[b][c] = ha[add - 1] 
    for cay in hng1:
        print(cay,end="")
    print()
    for cay in hng2:
        print(cay,end="")
    print()
    for cay in hng3:
        print(cay,end="")
    print()
    for cay in hng4:
        print(cay,end="")
    print()
    for cay in hng5:
        print(cay,end="")
    print()
    for cay in hng6:
        print(cay,end="")
    print()
    for cay in hng7:
        print(cay,end="")
    print()
    for cay in hng8:
        print(cay,end="")
    print()
    for cay in hng9:
        print(cay,end="")
    print()
    for cay in hng0:
        print(cay,end="")
    print()
else:
    print("Erorr: số không phù hợp , bạn thua!")