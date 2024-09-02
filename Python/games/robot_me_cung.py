#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# if right_is_clear()and wall_in_front():
#     turn_right()
# elif wall_on_front() and wall_on_right():
#     turn_left()
# elif wall_on_right() and front_is_clear():
#     move()
# elif right_is_clear() and front_is_clear():
#     move()
#     turn_right()

# P2:bai  Robot!
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# def super_jump():
#     turn_left()
#     #move()
# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     if wall_on_right() and wall_in_front():
#         super_jump()
#     if front_is_clear() and right_is_clear():
#         turn_right()
#         move()
#         turn_right()
#         move()
#     if wall_in_front() and right_is_clear():
#         turn_right()
#         move()
#         turn_right()
#         move()

# front_is_clear() and right_is_clear() == turn_right()

# right_is_clear()

# wall_on_right()

# wall_in_front()
# P3:Robot bai 8
# is_facing_north()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def left_is_clear():
#     turn_left()
#     turn_left()
#     if right_is_clear():
#         turn_left()
#         turn_left()
#         return True
#     else:
#         turn_left()
#         turn_left()
#         return False
# def wall_on_left():
#     turn_left()
#     turn_left()
#     if wall_on_right():
#         turn_left()
#         turn_left()
#         return True
#     else:
#         turn_left()
#         turn_left()
#         return False
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
        
#     if wall_on_right():
#         turn_left()
     
#     if wall_on_left():
#         turn_right()
       
#     if front_is_clear() and right_is_clear():
#         turn_right()
#         move()
      
#     if front_is_clear() and left_is_clear():
#         turn_left()
#         move()

#     if front_is_clear():
#         move()
        
