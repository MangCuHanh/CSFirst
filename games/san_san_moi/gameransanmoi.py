from os import system
import time
import keyboard
map = []
for c in range(20):
    dong = []
    for d in range(20):
        dong.append('🌳')
    map.append(dong)
# def in_map():
#     for c in map:
#         for d in map:
#             print('🌳',end="")
#         print()
    print()
map[9][3] = '🐰'
cot_dau_ran = [9]
hang_dau_ran = [3]
map[9][2] = '🐰'
cot_minh_ran = [9]
hang_minh_ran = [2]
while True:
    time.sleep(0.3)
    system('cls')
    # in_map()
    for cot in range(20):
        for hang in range(20):
            print(map[cot][hang],end="")    
        print()
    print()
    if keyboard.is_pressed('down'):
        map[cot_minh_ran[0]][hang_minh_ran[0]] = '🌳'
        cot_minh_ran[0] += 1
        map[cot_dau_ran[0]][hang_dau_ran[0]] = '🌳'
        cot_dau_ran[0] += 1
        map[cot_minh_ran[0]][hang_minh_ran[0]] = '🐰'
        map[cot_dau_ran[0]][hang_dau_ran[0]] = '🐰'
        if hang_dau_ran[0]-1 == hang_minh_ran[0]:
            map[cot_minh_ran[0]][hang_minh_ran[0]] = '🌳'
            map[cot_dau_ran[0]][hang_dau_ran[0]] = '🌳'
            hang_minh_ran[0] += 1
            cot_dau_ran[0] += 1
            map[cot_minh_ran[0]][hang_minh_ran[0]] = '🐰'
            map[cot_dau_ran[0]][hang_dau_ran[0]] = '🐰'
        if  hang_dau_ran[0]+1 == hang_minh_ran[0]:
            map[cot_minh_ran[0]][hang_minh_ran[0]] = '🌳'
            cot_dau_ran[0] += 1
            map[cot_dau_ran[0]][hang_dau_ran[0]] = '🌳'
            hang_minh_ran[0]-= 1
            map[cot_minh_ran[0]][hang_minh_ran[0]] = '🐰'
            map[cot_dau_ran[0]][hang_dau_ran[0]] = '🐰'
        if cot_dau_ran[0]-1 == cot_minh_ran[0]:
            map[cot_minh_ran[0]][hang_minh_ran[0]] = '🌳'
            map[cot_dau_ran[0]][hang_dau_ran[0]] = '🌳'
            cot_minh_ran[0] -= 1
            cot_dau_ran[0] += 1
            map[cot_dau_ran[0]][hang_dau_ran[0]] = '🐰'
            map[cot_minh_ran[0]][hang_minh_ran[0]] = '🐰'
    if keyboard.is_pressed('up'):
        cot_dau_ran[0] -=1
        cot_minh_ran[0] -=1
        if hang_dau_ran[0] -1 == hang_minh_ran[0]:
            hang_minh_ran[0] +=1
            cot_dau_ran[0]+=1
        if hang_dau_ran[0]+1 == hang_minh_ran[0]:
            hang_minh_ran[0]-=1
            cot_dau_ran[0]+=1
        if cot_dau_ran[0]-1 == cot_minh_ran[0]:
            cot_minh_ran[0]-=1
            cot_dau_ran[0]+=1  
    if keyboard.is_pressed('right'):
        hang_dau_ran[0]+=1
        hang_minh_ran[0]+=1
        if hang_dau_ran[0]-1 == hang_minh_ran[0]:
            hang_minh_ran[0]+=1
            cot_dau_ran[0]+=1
        if hang_dau_ran[0]+1 == hang_minh_ran[0]:
            hang_minh_ran[0]-=1
            cot_dau_ran[0]+=1
        if cot_dau_ran[0]-1 == cot_minh_ran[0]:
            cot_minh_ran[0]-=1
            cot_dau_ran[0]+=1  
    if keyboard.is_pressed('left'):
        print()