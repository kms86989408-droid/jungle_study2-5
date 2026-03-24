# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

n = int(input())
m = int(input())
edges = []

for _ in range(m):
    a, b = list(map(int, input().split()))
    edges.append((a, b))

visited = [False] * (n + 1)
graph = [ [] for _  in range(n + 1)]

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

def virus(x):
     visited[x] = True

     for nxt in graph[x]:
         if not visited[nxt]:
             virus(nxt)

virus(1)
print(sum(visited) - 1)