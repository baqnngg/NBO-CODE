# 1이 몇개 있는지 2가 몇개 있는지 확인하는 문제 (기억하는게 좋음)
n = list(map(int,input().split()))
t = []
for i in range(len(n)-1):
    if n[i] == 0: continue
    for j in range(i+1,len(n)):
        if n[i] != n[j]:
            t.append(j-i)
            t.append(n[i])
            break
        else: n[j] = 0
print(*t)