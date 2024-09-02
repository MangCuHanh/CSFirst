from os import system
import sys;
system('cls')
''
import random
# #Rock
# print("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)

# # Paper
# print("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)

# # Scissors
# print("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)
print("Chào mừng đến trò chơi kéo-búa-bao")
á = ["""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""","""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""]
a = int(input("bạn hãy nhập số 1:kéo 2:búa 3:bao:"))
if a <= 0 or a > 3:
    print("Erorr: Số này không có trong trò chơi và không có giá trị, bạn thua!")
    sys.exit()
else:  
    print("bạn ra" + á[a - 1])
s = random.randint(1,3)
print("máy ra" + á[s - 1])
if a == s:
    print("hòa nhau!")
elif a == 1 and s == 2:
    print("bạn thua!")
elif a == 3 and s == 2:
    print("bạn thắng!")
elif a == 2 and s == 3:
    print("bạn thua!")
elif a == 2 and s == 1:
    print("bạn thắng!")
elif a == 3 and s == 1:
    print("bạn thắng!")
elif a == 1 and s == 3:
    print("bạn thắng!")

