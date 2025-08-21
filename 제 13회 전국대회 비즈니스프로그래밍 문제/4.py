a = input()
b = input()
for i in b:
    if ord(i) >= 97: print(a[ord(i)-97],end="")
    else: print(" ",end="")