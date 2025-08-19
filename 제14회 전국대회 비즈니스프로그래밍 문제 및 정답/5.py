def wor(x,y):
    global cnt
    for i in range(3):
        st = graph[x][y]
        nx, ny = x,y
        for _ in range(4):
            if nx+dx[i] < n and ny+dy[i] < n:
                nx, ny = nx+dx[i], ny+dy[i]
                st += graph[nx][ny]
        if st[:4] == "wind" or st == "woman" or st == "stone":
            cnt += 1


n = int(input())
graph = [list(input()) for _ in range(n)]
cnt = 0

dx,dy = [1,1,0],[0,1,1]

for i in range(n):
    for j in range(n):
        if graph[i][j] in ["w","s"]:
            wor(i,j)
print(cnt)
