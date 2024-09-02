from os import system;  
import sys
import random;
import time;
from cauhoikydieu import dscauhoi,dscautraloi,dstraloi 
import nhackydieu
system('cls')
luoi = 5


vitri = random.randint(0,len(dscauhoi)-1)
# print(dscauhoi[vitri])
# print(dscautraloi[vitri])
print("Chào mừng đến với trò chơi chiếc nón kỳ diệu 🎭")
print("đang chuẩn bị câu hỏi...")
time.sleep(1)

nhapchu = False
# dschudung1 = ["T","r","a","n"]
# dschu1 = ["t","r","a","n"]
# dschu0 = ["j","a","m","e","s"," ","n","a","i","s","m","i","t","h"]


# nhap1kytu = input("hãy nhập 1 ký tự")
# if(dstraloi[1].count(nhap1kytu) > 0):
#     print(dstraloi[1])
#     print(dstraloi[1].index(nhap1kytu))
# else:
#     print("ko tim thay")
lanthang = 0

# dscauchutraloi = [dschu0,dschu1]
daugachduoi = []
for gach in dstraloi[vitri]:
    daugachduoi.append("_")
while luoi > 0:
    time.sleep(0.2)
    system('cls')
    á = daugachduoi.count("_")    
    print(dscauhoi[vitri])
    for dd in daugachduoi:
        print(dd,end="")
    print()
    if á == 0:
        print("bạn thắng!")
        nhackydieu.channel1.play(nhackydieu.tieng_win)
        time.sleep(8)
        sys.exit()
    print(f"bạn còn {luoi} đoán")
    chudoan = input(f"Hãy đoán một ký tự: ")
    a = dstraloi[vitri].count(chudoan)
    if a > 0:
        lanthang+=1            
        for a1 in range(a):
            for a2 in dstraloi[vitri]:
                if a2 == chudoan:
                    tam = 0
                    for dst in dstraloi[vitri]:
                        if chudoan == dst:
                            
                            #lay vi tri lan dau hoai
                            # chudoanso = dstraloi[vitri].index(chudoan)        
                    # daugachduoi[chudoanso] = chudoan
                            daugachduoi[tam] = dscautraloi[vitri][tam]
                        tam += 1                       
                    continue  
                
                    # for kytu in dstraloi[vitri]:
                    #     print(kytu)
        print("Đúng")
        nhackydieu.channel3.play(nhackydieu.tieng_tra_loi)
        time.sleep(1)
    else:
        luoi-=1
        print("Sai")
        nhackydieu.channel3.stop()
        nhackydieu.channel4.play(nhackydieu.tieng_tra_loi_sai)
        time.sleep(0.5)
        nhackydieu.channel4.stop()
        if luoi == 1:
            nhackydieu.channel5.play(nhackydieu.tieng_rung_ron)
        if luoi == 0:
            print(f"đó là {dscautraloi[vitri]}")
            print("bạn thua!")
            nhackydieu.channel2.play(nhackydieu.tieng_lose)
            time.sleep(3)
            