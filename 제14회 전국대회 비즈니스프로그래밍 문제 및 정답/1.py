a = int(input())
b = int(input())
c = ""
while a != 0:
    c = str(a % b) + c
    a //= b
print(c)