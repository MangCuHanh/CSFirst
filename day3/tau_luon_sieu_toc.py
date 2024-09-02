
bill = 0
print("chào mừng đến tàu lượn siêu tốc")
a = float(input("nhập chiều cao của bạn(m):"))
if a >= 1.20:
    print("bạn được vào")
    b = int(input("bạn bao nhiêu tuổi?"))
    if b < 12:      
       print("giá vé của bạn là 20đ")
       bill+= 20
    elif b <= 18:      
       print("giá vé của bạn là 30")
       bill+=30 
    elif b >= 45 and b <= 55:
        print("giá vé miễn phí ") 
        bill+= 0 
    else:      
       print("giá vé của bạn là 35đ")
       bill+=35
    f = input("bạn có chụp ảnh không?có hay không")
    if f == "có": 
       bill+= 10
    else:
       bill+= 0
else:
    print("bạn không được vào")
print("giá vé của bạn là:"+str(bill)+"đ")