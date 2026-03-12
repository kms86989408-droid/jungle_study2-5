# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

T = int(input())

for _ in range(T):
    n = int(input())

    a = n // 2
    b = n // 2

    while True:
        a_is_prime = True
        b_is_prime = True

        if a < 2:
            a_is_prime = False
        else:
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    a_is_prime = False
                    break

        if b < 2:
            b_is_prime = False
        else:
            for i in range(2, int(b ** 0.5) + 1):
                if b % i == 0:
                    b_is_prime = False
                    break

        if a_is_prime and b_is_prime:
            print(a, b)
            break

        a -= 1
        b += 1