from collections import defaultdict
from itertools import combinations
import bisect

def solution(info, query):
    # 지원자 정보를 저장할 딕셔너리
    data = defaultdict(list)

    # 지원자 정보 처리
    for applicant in info:
        details = applicant.split()
        score = int(details[-1])
        conditions = details[:-1]

        # 모든 조합을 만들어 딕셔너리에 추가
        for r in range(5):
            for comb in combinations(range(4), r):
                temp = ['-'] * 4
                for idx in comb:
                    temp[idx] = conditions[idx]
                data[''.join(temp)].append(score)

    # 딕셔너리 내 점수 리스트 정렬
    for key in data:
        data[key].sort()

    # 쿼리 처리
    result = []
    for q in query:
        details = q.replace(" and", "").split()
        key = ''.join(details[:-1])
        score = int(details[-1])

        # 해당 조건의 지원자 점수 리스트
        scores = data.get(key, [])

        # 이진 탐색으로 점수 조건 만족하는 개수 찾기
        index = bisect.bisect_left(scores, score)
        result.append(len(scores) - index)

    return result