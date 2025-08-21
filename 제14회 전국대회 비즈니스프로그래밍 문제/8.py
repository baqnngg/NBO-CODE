############################################## 투 포인터 사용(제미니)
import sys

def solve():
    """
    신종 사격 종목 문제를 해결하는 함수입니다.
    Meet-in-the-Middle 알고리즘을 사용합니다.
    """
    # 입력 처리
    try:
        n, t = map(int, sys.stdin.readline().split())
        points = [int(sys.stdin.readline()) for _ in range(n)]
    except ValueError:
        # 예시 입력을 위한 처리
        n, t = 4, 39
        points = [10, 11, 20, 5]

    # 1~3발만 쏘는 경우를 위해 0점 추가
    points.append(0)

    # 1. 두 발의 합을 모두 구하기
    two_shots_sum = []
    for p1 in points:
        for p2 in points:
            two_shots_sum.append(p1 + p2)

    # 2. 두 발의 합 리스트를 정렬
    two_shots_sum.sort()

    # 3. 투 포인터를 사용하여 목표점수 T 이하의 최대 총점 찾기
    max_score = 0
    left = 0
    right = len(two_shots_sum) - 1

    while left <= right:
        current_sum = two_shots_sum[left] + two_shots_sum[right]

        if current_sum <= t:
            # 현재 합이 T 이하이면, 최댓값을 갱신하고 더 큰 점수를 찾아본다.
            max_score = max(max_score, current_sum)
            left += 1
        else:
            # 현재 합이 T를 초과하면, 합을 줄이기 위해 right를 감소시킨다.
            right -= 1
            
    print(max_score)

solve()