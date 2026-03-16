# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920


### 이중for문 ###

# n = int(input())
# nums = list(map(int,input().split()))
# m = int(input())
# m_nums = list(map(int,input().split()))
# nums.sort()

# result = []

# for found in m_nums:
#     found = False
#     for num in nums:
#         if num == found :
#             found = True
#             break
#     if found:
#         result.append("1")
#     else:
#         result.append("0")

# print(result)

### 이분탐색 ###

n = int(input())
nums = list(map(int,input().split()))
m = int(input())
m_nums = list(map(int,input().split()))
nums.sort()

for i in range(m):
    left = 0
    right = len(nums) - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == m_nums[i]:
            found = True
            print(1)
            break
        elif nums[mid] > m_nums[i]:
            right = mid -1
            
        else:
            left = mid + 1
    if not found:
        print(0)