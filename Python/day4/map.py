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
map=[hng1,hng2,hng3,hng4,hng5,hng6,hng7,hng8,hng9,hng0]
print(f"{hng1}\n{hng2}{hng3}\n{hng4}{hng5}\n{hng6}{hng7}\n{hng8}{hng9}\n{hng0}")
a=input("bạn muốn nơi bạn cất giấu kho báu ở toa độ nào?")
b=int(a[0])
c=int(a[2])

map=[hng1,hng2,hng3,hng4,hng5,hng6,hng7,hng8,hng9,hng0]
# d = map[b-1]
# d[c] = 
ha = ["✖️","❌","❓","🔴"]
add = int(input("bạn muốn chọn hình nào?:\nnhập 1=✖️\nnhập 2=❌\nnhập 3=❓\nnhập 4=🔴:"))

hhh = map[b]
hhh[c] = ha
map[b][c] = ha[add - 1]
print(f"{map}") 
