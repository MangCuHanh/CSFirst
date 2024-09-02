from logo.hinhcaro import hinh;
from logo.huong import ban_huong_dan;
from os import system;
from logo.loai_chu import f;
import time;
import sys
system('cls')
print(hinh)
def re():
    asdf = input("bạn muốn chơi lại không?(Y/N)")
    if asdf == 'Y'or asdf == 'y':
        game()
    else:
        sys.exit()
def game():
    def kiem_tra_X_Win():
        if bang['1']=='X' and bang['4']=='X' and bang['7'] == 'X':
            return True    
        elif bang['2']=='X' and bang['5']=='X' and bang['8'] == 'X':
            return True
        elif bang['3']=='X' and bang['6']=='X' and bang['9'] == 'X':
            return True
        elif bang['1']=='X' and bang['2']=='X' and bang['3'] == 'X':
            return True
        elif bang['4']=='X' and bang['5']=='X' and bang['6'] == 'X':
            return True
        elif bang['7']=='X' and bang['8']=='X' and bang['9'] == 'X':
            return True
        elif bang['1']=='X' and bang['5']=='X' and bang['9'] == 'X':
            return True
        elif bang['3']=='X' and bang['5']=='X' and bang['7'] == 'X':
            return True

    def kiem_tra_X():
        if bang['1']=='X' and bang['4']=='X' and bang['7'] == 'X':
            print("X thắng!")
        elif bang['2']=='X' and bang['5']=='X' and bang['8'] == 'X':
            print("X thắng!")
        elif bang['3']=='X' and bang['6']=='X' and bang['9'] == 'X':
            print("X thắng!")
        elif bang['1']=='X' and bang['2']=='X' and bang['3'] == 'X':
            print("X thắng!")
        elif bang['4']=='X' and bang['5']=='X' and bang['6'] == 'X':
            print("X thắng!")
        elif bang['7']=='X' and bang['8']=='X' and bang['9'] == 'X':
            print("X thắng!")
        elif bang['1']=='X' and bang['5']=='X' and bang['9'] == 'X':
            print("X thắng!")
        elif bang['3']=='X' and bang['5']=='X' and bang['7'] == 'X':
            print("X thắng!")
    def kiem_tra_O():
        if bang['1']=='O' and bang['4']=='O' and bang['7'] == 'O':
            return True 
        elif bang['2']=='O' and bang['5']=='O' and bang['8'] == 'O':
            return True 
        elif bang['3']=='O' and bang['6']=='O' and bang['9'] == 'O':
            return True 
        elif bang['1']=='O' and bang['2']=='O' and bang['3'] == 'O':
            return True 
        elif bang['4']=='O' and bang['5']=='O' and bang['6'] == 'O':
            return True 
        elif bang['7']=='O' and bang['8']=='O' and bang['9'] == 'O':
            return True 
        elif bang['1']=='O' and bang['5']=='O' and bang['9'] == 'O':
            return True 
        elif bang['3']=='O' and bang['5']=='O' and bang['7'] == 'O':
            return True 
    def kiem_tra_hoa():       
        ConOTrong = 0
        for k in bang:
            if bang[k] == " ":
                ConOTrong += 1

        if ConOTrong == 0:
            return False
    def map():
        print("_______")
        print('|'+bang['1']+'|'+bang['2']+'|'+bang['3']+'|')
        print("|-+-+-|")
        print('|'+bang['4']+'|'+bang['5']+'|'+bang['6']+'|')
        print("|-+-+-|")
        print('|'+bang['7']+'|'+bang['8']+'|'+bang['9']+'|')
        print("=======")
    bang = {'1':' ','2':' ','3':' ',
            '4':' ','5':' ','6':' ',
            '7':' ','8':' ','9':' '        
    }
    
    
    jjj = input("xem hướng dẫn(h),vào chơi(s)")
    lan = 0
    if jjj == 's'or jjj == 'S':
        map()
        while lan < 9:
            if lan % 2 == 0 :
                nhập = str(input("bạn muốn đặt X ở đâu? "))
                aaa = bang.get(nhập)
                if aaa == None:
                    print("Error:kí tự không hợp lệ,bạn nên xem lại hướng dẫn")
                    time.sleep(1)
                    sys.exit()
                else:
                    if bang[nhập] == 'X' or bang[nhập] =='O':
                        print("đã có người đặt ở đó!")
                        map()
                        lan-=1
                    else:
                        bang[nhập] = 'X'
                        map()
                        if kiem_tra_X_Win():
                            print(f.renderText('X win'))
                            re()
            else:
                nhập = str(input("bạn muốn đặt O ở đâu? "))
                aaa = bang.get(nhập)
                if aaa == None:
                    print("Error:kí tự không hợp lệ,bạn nên xem lại hướng dẫn")
                    time.sleep(1)
                    sys.exit()
                else:
                    if bang[nhập] == 'O' or bang[nhập] =='X':
                        print("đã có người đặt ở đó!")
                        map()
                        lan-=1
                    else:
                        bang[nhập] = 'O'
                        map()
                        if kiem_tra_O():
                            print(f.renderText('O win'))
                            re()            
            lan +=1
    elif jjj == 'h'or jjj == 'H':
            system('cls')
            print(ban_huong_dan)
            time.sleep(5)
            system('cls')
            # chay()
            sys.exit()
    else:
        print("Error:chữ nhập không hợp lệ")
        sys.exit()
    print(f.renderText('No win'))
    re()
game()
# re()