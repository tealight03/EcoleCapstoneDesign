def solution(rows, columns, queries):
    # 초기 행렬 생성
    matrix = [[(i * columns) + j + 1 for j in range(columns)] for i in range(rows)]

    # 결과를 저장할 리스트
    answer = []

    # 회전 처리
    for query in queries:
        x1, y1, x2, y2 = [q - 1 for q in query]  # 0-index로 변환
        temp = matrix[x1][y1]  # 첫 번째 값을 임시 저장
        min_value = temp

        # 왼쪽 세로 이동
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i + 1][y1]
            min_value = min(min_value, matrix[i][y1])

        # 아래쪽 가로 이동
        for i in range(y1, y2):
            matrix[x2][i] = matrix[x2][i + 1]
            min_value = min(min_value, matrix[x2][i])

        # 오른쪽 세로 이동
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i - 1][y2]
            min_value = min(min_value, matrix[i][y2])

        # 위쪽 가로 이동
        for i in range(y2, y1, -1):
            matrix[x1][i] = matrix[x1][i - 1]
            min_value = min(min_value, matrix[x1][i])

        # 마지막 값 복원
        matrix[x1][y1 + 1] = temp

        # 최솟값 저장
        answer.append(min_value)

    return answer