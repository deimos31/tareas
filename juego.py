import os
os.system("clear")
print(" __________________________________________")
print("|                                          |")
print("|       !Welcome to Treasure Island¡       |")
print("|__________________________________________|")
print("                                            ")
print("                                            ")
print("                                            ")
print("********************************************")
print("*                                          *")
print("* ¡¡Your mission is to find the treasure!! *")
print("*                                          *")
print("********************************************")
print("                                            ")
print("                                            ")
print("                                            ")

direction = input("*Choose a direction (<=left/right=>)*: ").lower()
os.system("clear")
level2 = False
if direction == "left":
    level2 = True 
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!                                          !")
    print("!          You pass to level 2             !")
    print("!                                          !")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("                                            ")
    print("                                            ")
    print("                                            ")
    wtdo = input("°°° What do you want to do? °°° (swim or wait): ").lower()
    level3 =False
    if wtdo == "wait":
        os.system("clear")
        level3 = True
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("%                                          %")
        print("%          You pass to level 3             %")
        print("%                                          %")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("                                            ")
        print("                                            ")
        print("                                            ")
        wdoor = input("[ Choose a color to pass the dimensional portal ]: ").lower()
        win = False
        if wdoor == "yellow":
            os.system("clear")
            win = True
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            print("°                                          °")
            print("°          CONGRATULATION MATE             °")
            print("°                                          °")
            print("°           You are rich now               °")
            print("°     you have the secret treasure.        °")
            print("°                                          °")
            print("°                                          °")
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")         
        elif wdoor == "red":
                os.system("clear")
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
                print("°                                          °")
                print("°             FFFFFFFFF                    °")
                print("°             F                            °")
                print("°             FFFFFFFFF                    °")
                print("°             F                            °")
                print("°             F                            °")
                print("°             F                            °")
                print("°                                          °")
                print("°         You are burning in lava          °")
                print("°             GAME OVER hahaha             °")
                print("°                                          °") 
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        elif wdoor == "blue":
                    os.system("clear")
                    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
                    print("°                                          °")
                    print("°             FFFFFFFFF                    °")
                    print("°             F                            °")
                    print("°             FFFFFFFFF                    °")
                    print("°             F                            °")
                    print("°             F                            °")
                    print("°             F                            °")
                    print("°                                          °")
                    print("°     You died eaten by a large beast.     °")
                    print("°             GAME OVER hahaha             °")
                    print("°                                          °") 
                    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°") 
        elif not win:
                os.system("clear")
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
                print("°                                                    °")
                print("°             FFFFFFFFF                              °")
                print("°             F                                      °")
                print("°             FFFFFFFFF                              °")
                print("°             F                                      °")
                print("°             F                                      °")
                print("°             F                                      °")
                print("°                                                    °")
                print("° You are traveling to the centre of a massive star. °")
                print("°             GAME OVER hahaha                       °")
                print("°                                                    °") 
                print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    elif not level3:
        os.system("clear")
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
        print("°                                          °")
        print("°             FFFFFFFFF                    °")
        print("°             F                            °")
        print("°             FFFFFFFFF                    °")
        print("°             F                            °")
        print("°             F                            °")
        print("°             F                            °")
        print("°                                          °")
        print("°   You were attacked by a water monster.  °")
        print("°             GAME OVER hahaha             °")
        print("°                                          °") 
        print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
elif not level2:
    os.system("clear")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("°                                          °")
    print("°             FFFFFFFFF                    °")
    print("°             F                            °")
    print("°             FFFFFFFFF                    °")
    print("°             F                            °")
    print("°             F                            °")
    print("°             F                            °")
    print("°                                          °")
    print("°   You have fallen into a dark hole.      °")
    print("°             GAME OVER hahaha             °")
    print("°                                          °") 
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")