from os import system
system('cls')
sonhap = int(input("nhập 1 số lẻ:\n"))
a = 0
print()
while sonhap >= a:
    if a % 2 == 1:
        sokhoangtrang = (sonhap - a) // 2
        for kt in range(sokhoangtrang):
            print(" ",end="")
        for sao in range(a):
            print("*",end="")
        print()
    a += 1