from collections import defaultdict

def solution(gems):
    gem_types = len(set(gems))  # 보석의 종류 수
    gem_count = defaultdict(int)  # 현재 구간의 보석 개수

    start, end = 0, 0
    shortest = float('inf')  # 최소 구간 길이
    answer = [0, 0]  # 결과 구간

    while end < len(gems):
        gem_count[gems[end]] += 1
        end += 1

        # 모든 보석을 포함한 구간인지 확인
        while len(gem_count) == gem_types:
            if end - start < shortest:
                shortest = end - start
                answer = [start + 1, end]  # 1-indexed 결과 저장

            # 구간의 시작점 보석 제거
            gem_count[gems[start]] -= 1
            if gem_count[gems[start]] == 0:
                del gem_count[gems[start]]
            start += 1

    return answer