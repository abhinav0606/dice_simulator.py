import random
w=random.randint(1,6)
while True:
    if w==1:
        for i in range(5):
            if i==2:
                print("   0".rjust(5,"["),end="")
                print("    ".ljust(5,"]"))
            elif i==0 or i==4:
                print("----".rjust(5, "["), end="")
                print("----".ljust(5, "]"))
            else:
                print("    ".rjust(5,"["),end="")
                print("    ".ljust(5,"]"))
        p = input("roll again")
        if p == "y":
            w = random.randint(1, 6)
        else:
            break

    elif w==4:
        for i in range(5):
            if i==0 or i==4:
                print("----".rjust(5, "["), end="")
                print("----".ljust(5, "]"))
            elif i==1 or i==3:
                print("  0 ".rjust(5,"["),end="")
                print(" 0  ".ljust(5,"]"))
            else:
                print("    ".rjust(5, "["), end="")
                print("    ".ljust(5, "]"))
        p = input("roll again")
        if p == "y":
            w = random.randint(1, 6)
        else:
            break
    elif w==3:
        for i in range(5):
            if i==1 or i==2 or i==3:
                print("   0".rjust(5, "["), end="")
                print("    ".ljust(5, "]"))
            elif i==0 or i==4:
                print("----".rjust(5, "["), end="")
                print("----".ljust(5, "]"))
            else:
                print("    ".rjust(5, "["), end="")
                print("    ".ljust(5, "]"))
        p = input("roll again")
        if p == "y":
            w = random.randint(1, 6)
        else:
            break
    elif w==2:
        for i in range(5):
            if i == 0 or i == 4:
                print("----".rjust(5, "["), end="")
                print("----".ljust(5, "]"))
            elif i==2:
                print("  0 ".rjust(5, "["), end="")
                print(" 0  ".ljust(5, "]"))
            else:
                print("    ".rjust(5, "["), end="")
                print("    ".ljust(5, "]"))
        p = input("roll again")
        if p == "y":
            w = random.randint(1, 6)
        else:
            break
    elif w==5:
        for i in range(5):
            if i==0 or i==4:
                print("----".rjust(5, "["), end="")
                print("----".ljust(5, "]"))
            elif i==1 or i==3:
                print("  0 ".rjust(5, "["), end="")
                print(" 0  ".ljust(5, "]"))
            else:
                print("   0".rjust(5, "["), end="")
                print("    ".ljust(5, "]"))
        p = input("roll again")
        if p == "y":
            w = random.randint(1, 6)
        else:
            break
    else:
        for i in range(5):
            if i==1 or i==2 or i==3:
                print("  0 ".rjust(5, "["), end="")
                print(" 0  ".ljust(5, "]"))
            else:
                print("----".rjust(5, "["), end="")
                print("----".ljust(5, "]"))
        p = input("roll again")
        if p == "y":
            w = random.randint(1, 6)
        else:
            break
