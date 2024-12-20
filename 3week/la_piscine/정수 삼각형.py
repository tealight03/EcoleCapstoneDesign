def solution(triangle):
    # 아래에서부터 위로 합산
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 현재 위치에 아래층에서 가능한 최대 값을 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]