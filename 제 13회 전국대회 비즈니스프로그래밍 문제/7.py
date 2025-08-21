# *****************************
import heapq
import sys

# 빠른 입력을 위한 설정 (백준 등 온라인 저지에서 유용)
# input = sys.stdin.readline

def solve_robot():
    n = int(sys.stdin.readline())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # === 다익스트라 알고리즘 구현 ===

    min_costs = [[float('inf')] * n for _ in range(n)]

    pq = []

    min_costs[0][0] = grid[0][0]
    heapq.heappush(pq, (grid[0][0], 0, 0))

    dr = [-1, 1, 0, 0]  
    dc = [0, 0, -1, 1] 

    while pq:
        current_cost, r, c = heapq.heappop(pq)

        if current_cost > min_costs[r][c]:
            continue
        
        if r == n - 1 and c == n - 1:
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                new_cost = current_cost + grid[nr][nc]

                if new_cost < min_costs[nr][nc]:
                    min_costs[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
    
    print(min_costs[n-1][n-1])


solve_robot()