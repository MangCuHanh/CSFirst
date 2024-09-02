import keyboard


while True:
    if keyboard.is_pressed('down'):
        print("down")
    if keyboard.is_pressed('up'):
        print("up")
    if keyboard.is_pressed('left'):
        print("left")
    if keyboard.is_pressed('right'):
        print("right")