from os import system;
import sys
system('cls')
so = int(input("nhập một số:\n"))
sô = so - 1
só = 2
if so == 1:
    print("đây không phải là số nguyên tố !") 
    sys.exit()
if so == 2 or so == 3:    
    print("đây là số nguyên tố !")
    sys.exit()
for số in range(sô -1):
    if so % só == 0:
        print("đây không phải là số nguyên tố !")
        sys.exit()
    só+=1
print("đây là số nguyên tố !")  
        


















