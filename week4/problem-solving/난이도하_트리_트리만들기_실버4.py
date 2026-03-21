# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

n, m = map(int, input().split())

cur  = 0 

for nxt in range(1, n):
    print(cur,nxt)
    if cur < n - m:
        cur += 1
