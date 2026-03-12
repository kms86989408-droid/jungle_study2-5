# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    students = nums[0]
    scores = nums[1:]

    avg = sum(scores)/students
    count = 0

    for score in scores:
        if score > avg:
             count += 1

    ratio = (count / students) * 100
    print(f"{ratio:.3f}%")