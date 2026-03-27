# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    dist[0][0] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        r, c = queue.popleft()

        if r == n - 1 and c == m - 1:
            return dist[r][c]
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if maze[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

print(bfs())