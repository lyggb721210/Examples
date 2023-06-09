# -*-coding:utf8;-*-
"""
邮箱：lyggb721210@163.com
作者：yxr / lyggb721210
当前版本：V0.91
Email: lyggb721210@163.com
Author: yxr / lyggb721210
Current version: V0.91
"""

import map
import language as l
import os
import time


def clear(system):
    if system == "posix":
        os.system("clear")
    elif system == "nt":
        os.system("cls")


# end def

if __name__ == "__main__":
    #check save
    if os.path.exists("save.txt"):
        try :
            f = open("save.txt", "r")
            save = f.readlines()
            if float(save[0][0:3]) >= 2.2 and float(save[0][0:3])<=2:
                l.display_message(l.message.get("menu"), l.language)
                lever = 0
                l.display_message(l.message.get("save_load_err1"), l.language)
            elif float(save[0][0:3]) < 2.2 and float(save[0][0:3])>=2:
                l.display_message(l.message.get("menu"), l.language)
                lever = int(save[2][0:2])
                if l.language == "1":
                    print(" 3.继续游戏")
                else:
                    print(" 3.Continue the game")
        except:
            l.display_message(l.message.get("menu"), l.language)
            lever = 0
            l.display_message(l.message.get("save_load_err1"), l.language)
    else:
        l.display_message(l.message.get("menu"), l.language)

    lastprint = "  "
    a = input("")
    if a == "1":
        lever = 0
    inmap = map.map[lever]
    if a == "1" or a=="3":
        while True:
            q=input( l.display_message(l.message.get("check_autosafe"), l.language))
            if q == "y" or q=="Y" or q=="":
                autosave = True
                break
            elif q == "N" or q=="n":
                autosave = False
                break
        while True:
            clear(os.name)
            c = 0
            outmap = ""
            while c != len(inmap):
                outmap = outmap + inmap[c]
                c = c + 1
            print(outmap)
            print(lastprint)
            l.display_message(l.message.get("in_game"), l.language)
            b = input("")
            if b == "w" or b=="W":
                add = inmap.index("😊")
                acd = add - inmap.index("\n") - 1
            elif b == "a" or b=="A":
                add = inmap.index("😊")
                acd = add - 1
            elif b == "d" or b=="D":
                add = inmap.index("😊")
                acd = add + 1
            elif b == "s" or b=="S":
                add = inmap.index("😊")
                acd = add + inmap.index("\n") + 1
            else:
                lastprint = l.get_message("err").get(l.language)
                continue
            if acd <= 0:
                lastprint = l.get_message("hit_wall").get(l.language)
            elif acd > 0:
                if inmap[acd] == "🧱":
                    lastprint = l.get_message("hit_wall").get(l.language)
                elif inmap[acd] == "🔲":
                    lastprint = "  "
                    inmap[add] = "🔲"
                    inmap[acd] = "😊"
                elif inmap[acd] == "🚪":
                    while True:
                        clear(os.name)
                        l.display_message(l.message.get("lever_end"), l.language)
                        if autosave:
                            f = open("save.txt", "w")
                            print("2.1\n"+
                            "这是一个存档文件（McroP）。  This is a save file for McroP\n"+
                            str(lever + 1),sep="",end="",file=f)
                            f.close()
                            l.display_message(l.message.get("autosafed"), l.language)
                        a = input()
                        clear(os.name)
                        if a == "1":
                            if lever < len(map.map) - 1:
                                lever = lever + 1
                                inmap = map.map[lever]
                                break
                            elif lever >= len(map.map) - 1:
                                l.display_message(l.message.get("end"), l.language)
                                exit()
                        elif a == "2":
                            exit()
    elif a == "2":
        l.display_message(l.message.get("help"), l.language)
    else:
        l.display_message(l.message.get("input_err"), l.language)
