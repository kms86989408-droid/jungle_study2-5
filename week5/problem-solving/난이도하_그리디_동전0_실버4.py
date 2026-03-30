# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

n = list(map(int, input().split()))
m = n[0]
price = n[1]
coins = []
total_coin = 0

for i in range(m):
    k = int(input())
    coins.append(k)

coins.reverse()

for coin in coins:
    count = price // coin
    price = price % coin

    if count > 0:
        total_coin += count

print(total_coin)