from os import system
import sys;
system('cls')
''
import random

chu = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
so = ['1','2','3','4','5','6','7','8','9','0']
ki = ['!','@','#','$','%','^','&','*','(',')','_','+','=','~']
ki_tu = [chu,so,ki]
print("Chào mừng đến với chương trình tạo mật khẩu phức tạp!") 
kituchu = int(input("bạn muốn mật khẩu có bao nhiêu chữ cái?\n"))
kituso = int(input("bạn muốn mật khẩu bao nhiêu chữ số?\n"))
kitudatbiet = int(input("bạn muốn mật khẩu của bạn bao nhiêu kí tự đặt biệt?\n"))
kq = []
for j in range(kituchu):
    chungaunhien = random.randint(0,len(chu) - 1)
    kq.append(chu[chungaunhien])
for a in range(kituso):
    songaunhien = random.randint(0,len(so) - 1)
    kq.append(so[songaunhien])
for s in range(kitudatbiet):
    kingaunhien = random.randint(0,len(ki) - 1)
    kq.append(ki[kingaunhien])    
random.shuffle(kq)
print(f"\nĐây là mật khẩu:")

# lan = 0
# for jjjjjj in range(len(kq)):
#     print(kq[lan],end="")
#     lan+=1

# for jjjjjj in range(len(kq)):
#     print(kq[jjjjjj],end="")

for jjjjjj in kq:
    print(jjjjjj,end="")