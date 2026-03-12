# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

n = int(input())
nums = list(map(int, input().split()))
count = 0 

for i in range(n):
    if nums[i] < 2 :
        continue

    is_prime = True
    for j in range(2, nums[i]):
        if nums[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print(count)