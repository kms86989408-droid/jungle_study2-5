# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

n = input().strip()

# parts = n.split("-")
# answer = sum(int(x) for x in parts[0].split("+"))

# for part in parts[1:]:
#     answer -= sum(int(x) for x in parts.split("+"))
# print(answer)
# =======================================
parts = n.split("-")
answer = 0

first_num = parts[0].split("+")
for num in first_num:
    answer += int(num)

for part in parts[1:]:
    sum = 0
    p_num = part.split("+")

    for num in p_num:
        sum += int(num)
    
    answer -= sum
print(answer)
# =======================================