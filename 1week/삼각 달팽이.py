def solution(n):
    # 삼각형 배열 초기화
    triangle = [[0] * i for i in range(1, n + 1)]

    # 방향 설정 (아래, 오른쪽, 왼쪽 위 대각선)
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    x, y = 0, 0  # 시작 위치
    direction = 0  # 초기 방향 (아래)
    num = 1  # 삼각형에 채울 숫자

    while num <= n * (n + 1) // 2:  # 채워야 할 숫자의 범위
        triangle[x][y] = num
        num += 1

        # 다음 위치 계산
        nx, ny = x + dx[direction], y + dy[direction]

        # 범위를 벗어나거나 이미 숫자가 채워져 있는 경우 방향 전환
        if nx < 0 or ny < 0 or nx >= n or ny >= len(triangle[nx]) or triangle[nx][ny] != 0:
            direction = (direction + 1) % 3
            nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny

    # 결과를 일차원 리스트로 변환하여 반환
    result = []
    for row in triangle:
        result.extend(row)

    return result