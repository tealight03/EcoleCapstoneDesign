def solution(strings, n):
    # 정렬 기준: n번째 문자, 동일하면 전체 문자열 사전순
    return sorted(strings, key=lambda x: (x[n], x))