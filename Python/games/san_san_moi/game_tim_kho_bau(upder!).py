from os import system
# from playsound import playsound
import time
import winsound
import keyboard
import random
import sys
from pygame import mixer  # Load the popular external library
lan_thang = 0
system('cls')
# system('cls')
print("Chào mừng đến với đảo kho báu!")
map = []
print("đây là map")
for d in  range(20):  
        dong = [] 
        for d in range(20):
            dong.append("🌳")
            print("🌳",end="")  
        map.append(dong)
        print()
cot_giau_kho_bau = random.randint(2,20 - 1)
hang_giau_kho_bau = random.randint(2,20 - 1) 
map[cot_giau_kho_bau][hang_giau_kho_bau] = '❌'
map[0][0] = '👦'
cot_dau_nguoi = [0]
hang_dau_nguoi = [0]
cot_dau_nguoi_hien_tai = cot_giau_kho_bau
hang_dau_nguoi_hien_tai = hang_giau_kho_bau
print("hãy đi đến dấu ❌")
time.sleep(2)

mixer.init()
mixer.music.load('C:\\Users\\Gamer\\Downloads\\victory-mario-series-hq-super-smash-bros.mp3')
# mixer.music..load('C:\\Users\\Gamer\\Downloads\\victory-mario-series-hq-super-smash-bros.mp3')
system('cls')
# print
while True: 
    time.sleep(0.3)
    system('cls')
    print()
    for cot in range(20):
        for hang in range(20):
            print(map[cot][hang],end="")    
        print()
    print()
    if keyboard.is_pressed('down'):
        frequency = 2990  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        if cot_dau_nguoi[0] ==  19:
            print("Error: bạn không thể đi xuống nữa,bạn thua!")
            break
        map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '🌳'
        cot_dau_nguoi[0] += 1
        
        for dau in range(len(cot_dau_nguoi)):
            map[cot_dau_nguoi[dau]][hang_dau_nguoi[dau]] ='👦'
        # map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '👦'
    if keyboard.is_pressed('up'):
        frequency = 3100  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        if cot_dau_nguoi[0] == 0:
            print("Error: bạn không thể đi lên nữa,bạn thua!")
            break
        map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '🌳'
        cot_dau_nguoi[0] -= 1
        map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '👦'
    if keyboard.is_pressed('left'):
        frequency = 2710  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        if hang_dau_nguoi[0] == 0:
            print("Error: bạn không thể đi qua trái nữa,bạn thua!")
            break
        # while hang_dau_nguoi > 0:
        map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '🌳'
        hang_dau_nguoi[0] -= 1
        map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '👦'
    if keyboard.is_pressed('right'):
        frequency = 4000  # Set Frequency To 2500 Hertz
        duration = 200  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)        
        if hang_dau_nguoi == 19:
            print("Error: bạn không thể qua phải nữa,bạn thua!")
            break
        map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '🌳'
        hang_dau_nguoi[0] += 1
        map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '👦'
    if map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] == map[cot_giau_kho_bau][hang_giau_kho_bau]:
        # map[cot_dau_nguoi_hien_tai][hang_dau_nguoi_hien_tai] = '👦'

        cot_dau_nguoi.append(cot_giau_kho_bau)
        hang_dau_nguoi.append(hang_giau_kho_bau)

        # map[cot_dau_nguoi[0]][hang_dau_nguoi[0]] = '👦'
        cot_giau_kho_bau = random.randint(2,20 - 1)
        hang_giau_kho_bau = random.randint(2,20 - 1) 
        map[cot_giau_kho_bau][hang_giau_kho_bau] = '❌'
        lan_thang +=1
        if lan_thang == 5:
            print("bạn thắng!")
            mixer.music.play()
            time.sleep(8)
            sys.exit()
    if keyboard.is_pressed('q'):
        print("hẹn gặp lại!")
        time.sleep(2)
        sys.exit()














# print("Error: số quá lớn không hợp lệ!")
# sys.exit()

# while True:
#     if keyboard.is_pressed('down'):
#         print("down")
#     if keyboard.is_pressed('up'):
#         print("up")
#     if keyboard.is_pressed('left'):
#         print("left")
#     if keyboard.is_pressed('right'):
#         print("right")

# for d in  range(iii):  
#     dong = [] 
#     for d in range(iii):
#         dong.append("🌳")
#         print("🌳",end="")
#         map.append(dong)
#         print()