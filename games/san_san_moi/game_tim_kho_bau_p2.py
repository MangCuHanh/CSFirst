from os import system
# from playsound import playsound
import time
import winsound
import keyboard
import random
import sys
from pygame import mixer  # Load the popular external library



def in_ban_do(map):
    for c in range(len(map)):  
        for d in range(len(map)):
            print(map[c][d],end="")  
        print()

def cap_nhat_vitri_con_ran(con_ran, cot_moi, hang_moi):
    del(con_ran[-1])
    con_ran.insert(0, (cot_moi, hang_moi))

def CapNhat_ConRan_tren_map(map, conran):
    for x,y in conran:
        map[x][y] = "👦"


lan_thang = 5
system('cls')
# system('cls')
print("Chào mừng đến với đảo kho báu!")
print("đây là map")
map = []

for d in  range(20):  
    dong = [] 
    for d in range(20):
        dong.append("🌳")
    map.append(dong)

cot_giau_kho_bau = random.randint(2,20 - 1)
hang_giau_kho_bau = random.randint(2,20 - 1) 

cot_giau_kho_bau = 6
hang_giau_kho_bau = 0

map[cot_giau_kho_bau][hang_giau_kho_bau] = '❌'

con_ran = [(0,0)]
map[0][0] = '👦'

in_ban_do(map)

print("hãy đi đến dấu ❌")
time.sleep(2)

mixer.init()

channel1 = mixer.Channel(0) # argument must be int
channel2 = mixer.Channel(1)
tieng_win = mixer.Sound('C:\\Users\\Gamer\\Downloads\\victory-mario-series-hq-super-smash-bros.mp3')
tieng_lose = mixer.Sound('C:\\Users\\Gamer\\Downloads\\pue-pue-pue_ltDwNu9.mp3')

# tieng_win..load('C:\\Users\\Gamer\\Downloads\\victory-mario-series-hq-super-smash-bros.mp3')
# mixer.music..load('C:\\Users\\Gamer\\Downloads\\victory-mario-series-hq-super-smash-bros.mp3')
system('cls')

column_of_snake_head = 0
row_of_snake_head = 0

# print
while True: 
    time.sleep(0.3)
    system('cls')
    print() 
    
    
    in_ban_do(map)

    print()
    if keyboard.is_pressed('down'):
        frequency = 2990  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        column_of_snake_head, row_of_snake_head = con_ran[0]
        if column_of_snake_head ==  19:
            print("Error: bạn không thể đi xuống nữa,bạn thua!")
            break

        column_of_snake_head +=1
        cot_DuoiConRan, hang_DuoiConRan = con_ran[-1]
        map[cot_DuoiConRan][hang_DuoiConRan] = "🌳"
        cap_nhat_vitri_con_ran(con_ran=con_ran, cot_moi=column_of_snake_head, hang_moi=row_of_snake_head)
        CapNhat_ConRan_tren_map(map, conran=con_ran)

    if keyboard.is_pressed('up'):
        frequency = 3100  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    #     if cot_dau_nguoi[0] == 0:
    #         print("Error: bạn không thể đi lên nữa,bạn thua!")
    #         break
    #     map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '🌳'
    #     cot_dau_nguoi[0] -= 1
    #     map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '👦'
    # if keyboard.is_pressed('left'):
    #     frequency = 2710  # Set Frequency To 2500 Hertz
    #     duration = 200  # Set Duration To 1000 ms == 1 second
    #     winsound.Beep(frequency, duration)
    #     if hang_dau_nguoi[0] == 0:
    #         print("Error: bạn không thể đi qua trái nữa,bạn thua!")
    #         break
    #     # while hang_dau_nguoi > 0:
    #     map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '🌳'
    #     hang_dau_nguoi[0] -= 1
    #     map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '👦'
    # if keyboard.is_pressed('right'):
    #     frequency = 4000  # Set Frequency To 2500 Hertz
    #     duration = 200  # Set Duration To 1000 ms == 1 second
    #     winsound.Beep(frequency, duration)        
    #     if hang_dau_nguoi == 19:
    #         print("Error: bạn không thể qua phải nữa,bạn thua!")
    #         break
    #     map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '🌳'
    #     hang_dau_nguoi[0] += 1
    #     map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '👦'
    if map[column_of_snake_head][row_of_snake_head] == map[cot_giau_kho_bau][hang_giau_kho_bau]:
        # map[cot_dau_nguoi_hien_tai][hang_dau_nguoi_hien_tai] = '👦'

        con_ran.append((cot_giau_kho_bau, hang_giau_kho_bau))
        
        cot_giau_kho_bau = random.randint(2,20 - 1)
        hang_giau_kho_bau = random.randint(2,20 - 1) 
        map[cot_giau_kho_bau][hang_giau_kho_bau] = '❌'
        lan_thang +=1
        if lan_thang >= 5:
            print("bạn thắng!")
            channel1.play(tieng_win)
            # mixer.music.play()
            time.sleep(8)
            sys.exit()

        CapNhat_ConRan_tren_map(map, conran=con_ran)


    if keyboard.is_pressed('q'):
        print("hẹn gặp lại!")
        time.sleep(2)
        sys.exit()









