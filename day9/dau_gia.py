# from logo_daugia import logo;
# from os import system;
# system('cls')
# nguoi_dau_gia = {}
# print(logo)
# print("Chào mừng đến buổi đấu giá!")
# ten = input("Bạn tên gì?")
# tien = input("bạn muốn đấu giá bao nhiêu?")
# nguoi_dau_gia[ten] = tien 

# 2 số có tổng là 54, số thứ nhất nhân 4 bằng số thứ hai nhân 5
# tìm số thứ 2

so1 = 54
so2 = 0
while so1 < 0:
    while so2 > 54: 
        print()
        t1 = so1 + so2 == 54
        t2 = so1 * 4 == so2 *5
        t3 = t2 and t1
        if t3 :
            print(f"so1 là {so1}, so2 là {so2}")
            break
        else:
            so2 += 1
            # continue
    so1 -= 1
        
            
    