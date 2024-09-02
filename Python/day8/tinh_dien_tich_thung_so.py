import math

#1
# import logo_paint

#2
from logo_paint import logo


def tinh_thung_son(cao,rong):
    tong = (cao*rong)/5
    return tong
#1
# print(logo_paint.logo)
#2
print(logo)

cao = int(input("nhập chiều cao của bức tường: "))
rong = int(input("nhập chiều rộng của bức tường: "))
a = tinh_thung_son(cao, rong)
print(f"cần mua {math.ceil(a)} thùng sơn")