import keyboard
from os import system
import time
from termcolor import colored
import random
import keyboard
import pygame

system('cls')

convit = ["  __", 
       "_( .)>",
       "\___)"]
dsMau = ['red','blue','yellow','green','black','white',"light_blue"]
may =["          .-~~~-.",
      "  .- ~ ~-(       )_ _",
      " /                     ~ -.",
      "|                           \\",
      " \                         .'",
      "   ~- . _____________ . -~"] 

khoangtrang = 0
sosong = 80
khoangtrangcuamay = 0
bam = False
while True:
        if khoangtrang * 2 >= sosong:
                khoangtrang = 0
        if keyboard.is_pressed('f'):
                bam = True
        if khoangtrangcuamay * 2 - 14 >= sosong:
                khoangtrangcuamay = 0
        ViTriMau = random.randint(0, len(dsMau) -1)
        for d in may:
                for kc in range(khoangtrangcuamay):
                        # if khoangtrang % 3 == 0:
                        print(" ",end="")        
                print(d)
        khoangtrangcuamay += 1        
        for dong in range(0,len(convit)):
                print(convit[dong],end="")
                        # for kt in range(khoangtrang):
                if dong == 1:
                        if bam:
                                for kt in range(khoangtrang):
                                        print("  ",end="")
                                print("-",end="") #6
                print()
                        # print("-")
        # print(colored(dong,dsMau[ViTriMau] ))
        khoangtrang += 1
        for song in range(sosong):
                if (song + khoangtrang) % 2 == 0:
                        print(colored('~','blue'),end="")
                else:
                        print(colored('-','blue'),end="")
        time.sleep(0.1)
        system('cls')