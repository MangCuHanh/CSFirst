from os import system
# from termcolor import colored

system('cls')
''
import random 

# xingau1 = random.randint(1,6)
# xingau2 = random.randint(1, 6)

# a = random.random()

# print(a)

# print(f"{xingau1} {xingau2}")

#nhap 1 so
#tinh toan de biet so do la chan hay le

# xingau = random.randint(1,100)
# print(xingau)

# isChan = xingau % 2 == 0

# if isChan:
#     print("số chẵn")
# else:
#     print("số lẻ")  


# TinhThanh = ["HCM", "Hà Nội", "Bình Dương", "Bình Định", "Vĩnh Long"]
# # print(TinhThanh)
# # print(TinhThanh[0])
# print(TinhThanh[1])
# # print(TinhThanh[-2])

# TinhThanh[1] = "Hà Bá"
# print(TinhThanh[1])

# TinhThanh.append("Hà Giang")
# TinhThanh.extend(["aaa", "bbb"])
# print()
# s = ["Trương Kiến Văn","Trương Gia Mẫn","Hoa Nguyễn Minh Hoàng","Nguyễn Phú Khánh","Hoa Nguyễn Phúc An","Trương Đắc Tôn","Trần Quốc Mỹ Tiên","Lý Ngọc Kiều","Tuấn Khang tiki"]
# a = random.randint(0, len(s) - 1)
# print(f"bạn sẽ trả tiền hôm nay là: {s[a]}")
# if s == 0:
#     print("Trương Gia Mẫn")
# elif s == 1:
# #     print("Trương Kiến Văn")
# TinhThanh = ["HCM", "Hà Nội", "Bình Dương", "Bình Định", "Vĩnh Long","Hạ Long","Vũng Tàu","Nha Trang","Phan Thiết","Cần Thơ","Mũi Né","Kiên Giang","Cà Mau"]
# print(f"Nơi du lịch đã được chọn là:{TinhThanh[random.randint(0, len(TinhThanh) - 1)]}")

# a =int(input("bạn hãy nhập 6 số của tờ vé số:"))
# print(a)
# b =random.randint(1,9)
# c =random.randint(1,9)
# d =random.randint(1,9)
# e =random.randint(1,9)
# f =random.randint(1,9)
# g =random.randint(1,9)
# print(b,c,d,e,f,g)

#bài của Jun
a = input("bạn hãy nhập tờ vé số của bạn:")
sothu1 =random.randint(0,9)
sothu2 =random.randint(0,9)
sothu3 =random.randint(0,9)
sothu4 =random.randint(0,9)
sothu5 =random.randint(0,9)
sothu6 =random.randint(0,9)

print(f"Số nhà đài của hôm nay là: {sothu1}{sothu2}{sothu3}{sothu4}{sothu5}{sothu6}")

CacSoGiongNhau = 0

if sothu1 == a[0]:
    CacSoGiongNhau += 1
if sothu2 == a[1]:
    CacSoGiongNhau += 1
if sothu3 == a[2]:
    CacSoGiongNhau += 1
if sothu4 == a[3]:
    CacSoGiongNhau += 1
if sothu5 == a[4]:
    CacSoGiongNhau += 1
if sothu6 == a[5]:
    CacSoGiongNhau += 1

if CacSoGiongNhau == 6:
    print("bạn trúng độc đắc")    
elif CacSoGiongNhau == 5:
    print("bạn trúng 30 000 000đ")
elif CacSoGiongNhau == 4:
    print("bạn trúng 15 000 000đ")
elif CacSoGiongNhau < 2:
    print("chúc may mắn lần sau!")


# j = random.randint(100000,999999)
# print(j)
# if a == j:
#     print("bạn trúng số độc đắc:2 000 000 000đ")
# elif a == j([0][1]):
#     print("bạn trúng số:30 000 000đ")
# elif a == j[0,1,2,3]:
#     print("bạn trúng số:15 000 000đ")
# else:
#     print("chúc may mắn lần sau!")





































