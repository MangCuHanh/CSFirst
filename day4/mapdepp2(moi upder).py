from os import system
import sys;
system('cls')
iii = int(input("bạn muốn kích thước của bản đồ là bao nhiêu?\n"))
map = []
if iii <= 30:
    system('cls')
    for d in  range(iii):  
        dong = [] 
        for d in range(iii):
            dong.append("🌳")
            print("🌳",end="")
        map.append(dong)
        print()

else:
    print("Error: số quá lớn không hợp lệ!")
    sys.exit()

a = int(input(f"bạn muốn kho báu của bạn được giấu ở hàng nào?(1 đến {iii})\n"))
s = int(input(f"bạn muốn kho báu của bạn được giấu ở cột nào?(1 đến {iii})\n"))
ha = ["✖️","❌","❓","🔴"]
add = int(input("bạn muốn chọn hình nào?:\nnhập 1 = ✖️\nnhập 2 = ❌\nnhập 3 = ❓\nnhập 4 = 🔴:\n"))
if add <= 4:
    map[a - 1][s - 1] = ha[add - 1] 
    for d in  range(iii):  
        for c in range(iii):
            print(map[d][c],end="")
        print()
else:
    print("Erorr: số lớn quá không hợp lệ!")