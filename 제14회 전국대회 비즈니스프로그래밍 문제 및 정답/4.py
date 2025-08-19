########################### 공약수들의 합을 구하는 문제 -> math 함수를 사용 : for문 사용시 데드락
import math

def sum_common_divisors(a, b):
    g = math.gcd(a, b)
    total = 0
    root = int(math.isqrt(g))
    for i in range(1, root + 1):
        if g % i == 0:
            total += i
            if i != g // i:
                total += g // i
    return total

A, B = map(int, input().split())
print(sum_common_divisors(A, B))
