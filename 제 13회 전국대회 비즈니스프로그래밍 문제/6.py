def haha(sn):
    visited[sn] = 1
    for i in adj_list[sn]:
        if visited[i] == 0:
            haha(i)
n = int(input())
p = int(input())
adj_list = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(p):
    s,e = map(int,input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

for i in range(n+1):
    adj_list[i].sort()

haha(int(input()))
print(visited.count(1)-1)