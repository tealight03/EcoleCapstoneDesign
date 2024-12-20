def solution(N, number):
    # 동적 계획법을 위한 집합 리스트 초기화
    dp = [set() for _ in range(9)]  # N을 1번 사용한 경우부터 8번 사용한 경우까지

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N을 i번 반복한 수 (예: 5, 55, 555, ...)

        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        if number in dp[i]:
            return i

    return -1