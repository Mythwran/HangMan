# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 02:19:39 2019

@author: Mythwran
"""

from random import randint
import os

#asilan adamin cizimleri
hang_man = ["""
     ________
     |      |
            |
            |
            |
            |""","""
     ________
     |      |
     O      |
            |
            |
            |""","""
     ________
     |      |
     O      |
     |      |
            |
            |""","""
     ________
     |      |
     O      |
    /|      |
            |
            |""","""
     ________
     |      |
     O      |
    /|\     |
            |
            |""","""
     ________
     |      |
     O      |
    /|\     |
    /       |
            |""","""
     ________
     |      |
     O      |
    /|\     |
    / \     |
            |"""]

#Ana belirtecler
os.system('cls')
name = str(input("Your name: ") or "Player").capitalize()
os.system('cls')
live = 0
words = ["telephone" , "computer" , "joystick" , "headset" , "mouse" , 
         "harddisk" , "charger" , "gamepad" , "modem" , "adapter" , "camera"]
g_word = words[randint(0,4)].upper()

#Baslangic ekrani (taslak)
#print(g_word) #secilen kelime
print(f"Hello {name}.\n")
print("You have 6 lives left.")
print(hang_man[0] + "\n\n")
print("_ "*len(g_word) , end="")

#Oyunun ana mekanigi ve cizimi
lengt_g_word = len(g_word)
list_g_word = list(g_word[:])
entered_letters = []

while True:
    g = []
    g = list(str(input("\nPlease enter a letter: ") or ".").upper()[0])
    os.system('cls')
    print("\n")
    if g[0] in entered_letters:
        live = live + 1
    elif g[0] in list_g_word:
        entered_letters.append(g[0])
    else:
        live = live + 1
    c_live = 6 - live
    print(f"You have {c_live} lives left.")
    print(hang_man[live] + "\n\n")
    #kelime kontrolu
    list_g_word = list(g_word[:])
    c_list_g_words = list_g_word
    i=0
    while i < lengt_g_word:
        flag = False
        for a in entered_letters:
            if a == c_list_g_words[i]:
                print(f"{a} ", end='')
                i += 1
                flag = True
                break
        if flag == True:
            continue
        print("_ ", end='')
        i += 1
    set_entered_letters = set(entered_letters)
    set_g_word = set(g_word[:])
    if set_entered_letters == set_g_word:
        print(f"\n\nYou have won {name}!!!")
        break
    if live == 6:
        print(f"\n\nYou have lost {name} :(")
        print(f"\nThat was {g_word}")
        break
