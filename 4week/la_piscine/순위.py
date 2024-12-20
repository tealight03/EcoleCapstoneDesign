def solution(n, results):
    # 그래프 초기화
    wins = [[False] * (n + 1) for _ in range(n + 1)]

    # 결과 입력
    for winner, loser in results:
        wins[winner][loser] = True

    # 플로이드-워셜 알고리즘 적용
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if wins[i][k] and wins[k][j]:
                    wins[i][j] = True

    # 각 선수의 승패 기록을 확인
    answer = 0
    for i in range(1, n + 1):
        known_results = 0
        for j in range(1, n + 1):
            if wins[i][j] or wins[j][i]:
                known_results += 1

        if known_results == n - 1:
            answer += 1

    return answer