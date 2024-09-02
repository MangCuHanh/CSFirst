from logo.chu import tengame;
from os import system;
from random import randint;
system('cls')
print("Chào mừng đến game")
print(tengame)
a = input("Chế độ: nhập d(dễ),nhập t(trung bình),nhập k(khó),nhập s(siêu khó!)")
def de():
    dap_and = randint(1,100)
    print("chế độ từ 1-100")
    hoi = 0
    lan = 100
    while hoi != dap_and:
        hoi = int(input("Bạn hãy đoán số "))
        if hoi < dap_and:
            print("Đó là một số lớn hơn!")
        elif hoi > dap_and:
            print("Đó là một số nhỏ hơn!")
        elif hoi == dap_and:
            print("Bạn thắng!")
            print(f"Số điểm của bạn là: {lan}")
            break
        lan-=1
        print(f"bạn còn {lan} điểm")
def trungbinh():
    dap_ant = randint(1,10000)
    print("chế độ từ 1-10,000")
    lan = 100
    hoi = 0
    while hoi != dap_ant:
        hoi = int(input("Bạn hãy đoán số "))
        if hoi < dap_ant:
            print("Đó là một số lớn hơn!")
        elif hoi > dap_ant:
            print("Đó là một số nhỏ hơn!")
        elif hoi == dap_ant:
            print("Bạn thắng!")
            print(f"Số điểm của bạn là: {lan}")
            break
        lan-=1
        print(f"bạn còn {lan} điểm")
def kho():
    dap_ank = randint(1,100000)
    print("chế độ từ 1-100,000")
    hoi = 0
    lan = 100
    while hoi != dap_ank:
        hoi = int(input("Bạn hãy đoán số "))
        if hoi == dap_ank:
            print("Bạn thắng!")
            print(f"Số điểm của bạn là: {lan}")
            break
        elif hoi % 9 == 0 or hoi % 3 == 0 or hoi % 5 == 0:
            print("tôi không biết")
        elif hoi < dap_ank:
            print("Đó là một số lớn hơn!")
        elif hoi > dap_ank:
            print("Đó là một số nhỏ hơn!")
        lan-=1
        print(f"bạn còn {lan} điểm")
def skho():
    dap_ans = randint(1,100000000)
    print("chế độ từ 1-100,000,000")
    lan = 100
    hoi = 0
    while hoi != dap_ans:
        hoi = int(input("Bạn hãy đoán số "))
        if hoi < dap_ans:
            print("tôi không biết!")
        elif hoi > dap_ans:
            print("tôi không biết!")
        elif hoi == dap_ans:
            print("Bạn thắng!")
            print(f"Số điểm của bạn là: {lan}")
            break
        lan-=1
        print(f"bạn còn {lan} điểm")
if a.lower() == 'd':
    de()
elif a.lower() == 't':
    trungbinh()
elif a.lower() == 'k':
    kho()
elif a.lower() == 's':
    skho()