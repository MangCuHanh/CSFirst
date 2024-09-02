from os import system
system('cls')
import sys;
so_ngta_nhap = int(input("hãy nhập một số nhỏ hơn hoặc bằng 25\n"))
g = 0
a = 0
so_sao = 0
so_khoangtrang = 0
if so_ngta_nhap <= 25:
    print()                                                                           
    while so_ngta_nhap > a:
        so_sao = a + 1
        so_khoangtrang = so_ngta_nhap - a - 1
        for kt in range(so_khoangtrang):
            print(" ",end="")
        for sao in range(so_sao):
            print("*", end="")
        print()
        a+=1
    print()
    while so_ngta_nhap > g:
        so_sao = so_ngta_nhap - g 
        for j in range(so_khoangtrang):
            print(" ",end="")
        for saoo in range(so_sao):
            print("*",end="")
        print()
        g+=1
        so_khoangtrang = so_khoangtrang + 1


else:
    print("Error: số quá lớn, không hợp lệ!")
    sys.exit()