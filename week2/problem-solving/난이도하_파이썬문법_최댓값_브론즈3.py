# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

nums = []
for i in range(9):
    nums.append(int(input()))

max_nums = nums[0]
max_index = 0

for j in range(1, 9):
    if nums[j] > max_nums :
        max_nums = nums[j]
        max_index = j

print(max_nums)
print(max_index+1)