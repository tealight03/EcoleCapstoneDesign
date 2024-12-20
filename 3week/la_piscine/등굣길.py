def solution(m, n, puddles):
    # 2D DP 테이블 초기화
    dp = [[0] * m for _ in range(n)]

    # 시작점 초기화
    dp[0][0] = 1

    # 웅덩이를 1로 표시해 계산 제외
    for x, y in puddles:
        dp[y - 1][x - 1] = -1

    # DP 테이블 채우기
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                dp[i][j] = 0  # 웅덩이는 경로가 0개
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]  # 위쪽에서 오는 경로
                if j > 0:
                    dp[i][j] += dp[i][j - 1]  # 왼쪽에서 오는 경로

                dp[i][j] %= 1000000007

    return dp[n - 1][m - 1]