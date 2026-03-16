# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque

n = int(input())
card_stack = deque(range(1, n+1))
card_arry = []
    
while True:
    if len(card_stack) == 1:
        print(card_stack[0])
        break
    else :
        card_arry.append(card_stack.popleft())
        card_stack.append(card_stack.popleft())
        