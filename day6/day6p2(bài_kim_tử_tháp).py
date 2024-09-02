from os import system
import sys;
system('cls')
songtanhap = int(input("hãy nhập một số lẻ ,nhỏ hơn hoặc bằng 15 (không nhỏ hơn 5)\n"))
khoangcach = songtanhap - 3
soao = 1
a = -1
if khoangcach > 0:
    print()
    while khoangcach > a:                                                                                  
        khoangcach -= 1
        # print(f"khoangcach{khoangcach},soao{soao}")
        for kc in range(0,khoangcach):
            print(" ",end="")
        for sao in range(0,soao):
            print("*",end="")
        print()
        soao += 2
else: 
    print("Error: số quá giới hạn, không hợp lệ!")
