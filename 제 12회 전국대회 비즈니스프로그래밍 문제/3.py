#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
n = int(input())
p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))

count = [0,0]

if (n // p1[1]) * p1[0] < (n // p2[1]) * p2[0]:
    count[0] += n//p1[1]
    n %= p1[1]
    count[1] += n//p2[1]
    n %= p2[1]
else:
    count[1] += n//p2[1]
    n %= p2[1]
    count[0] += n//p1[1]
    n %= p1[1]

if n != 0:
    print("Not Full")
else:
    print(*count)