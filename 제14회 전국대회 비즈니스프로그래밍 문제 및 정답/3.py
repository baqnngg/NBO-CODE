special_symbols = "!@#$%^&*()_+"

n = input()
boolst = [False] * 4

for i in n:
    if 'A' <= i <= 'Z': boolst[0] = True
    elif 'a' <= i <= 'z': boolst[1] = True
    elif i in special_symbols: boolst[2] = True
    elif '0' <= i <= '9': boolst[3] = True

if boolst.count(False) >= 2: print("check your password")
elif boolst.count(False) == 0: print("accept")
elif boolst[0] == False: print("need uppercase")
elif boolst[1] == False: print("need lowercase")
elif boolst[2] == False: print("need special symbols")
elif boolst[3] == False: print("need number")
