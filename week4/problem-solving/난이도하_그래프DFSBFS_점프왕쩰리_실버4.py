# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

def dfs(r, c):
    if r >= n or c >= n: # 보드 밖으로 나가면 실패
        return False
    if board[r][c] == -1 : # 도착칸에 도착하면 성공
        return True
    if visited[r][c]:
        return False
    visited[r][c] = True
    jump = board[r][c]

    return dfs(r, c +jump) or dfs(r + jump, c)

if dfs(0,0):
    print("HaruHaru")
else:
    print("Hing")