########################################### 다익스트라
n, m = map(int, input().split())
INF = 1e8

graph = [[] for _ in range(n+1)]

for _ in range(m):
  u, v, w = map(int, input().split()) # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
  graph[u].append((v, w))             # 거리 정보와 도착노드를 같이 입력합니다.

def get_smallest_node():
  min_val = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_val and not visited[i]: 
      min_val = distance[i]
      index = i
  return index

def dijkstra(start, end):
  distance[start] = 0 # 시작 노드는 0으로 초기화
  visited[start] = True

  for i in graph[start]:
    distance[i[0]] = i[1] # 시작 노드와 연결된 노도들의 거리 입력
  
  for _ in range(n-1): 
    now = get_smallest_node() # 거리가 구해진 노드 중 가장 짧은 거리인 것을 선택
    visited[now] = True       # 방문 처리

    for j in graph[now]:
      if distance[now] + j[1] < distance[j[0]]: # 기존에 입력된 값보다 더 작은 거리가 나온다면,
        distance[j[0]]= distance[now] + j[1]    # 값을 갱신한다.

for i in range(int(input())):
    visited = [False] * (n+1)
    distance = [INF] * (n+1)
    a,b = map(int,input().split())
    dijkstra(a, b)
    if distance[b] == 100000000.0:
        print("INF")
    else:
        print(distance[b])