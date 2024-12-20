from collections import Counter

def solution(clothes):
    # 각 의상의 종류별로 개수를 세기
    clothes_count = Counter([kind for name, kind in clothes])

    # 조합 계산: (각 종류의 개수 + 1)을 모두 곱한 뒤, -1 (아무것도 입지 않은 경우 제외)
    combinations = 1
    for count in clothes_count.values():
        combinations *= (count + 1)

    return combinations - 1