def solution(n):
    def hanoi(n, start, end, via, result):
        if n == 1:
            # 원판을 시작 기둥에서 목표 기둥으로 이동
            result.append([start, end])
        else:
            # n-1개의 원판을 중간 기둥(via)로 이동
            hanoi(n-1, start, via, end, result)
            # 가장 큰 원판을 목표 기둥으로 이동
            result.append([start, end])
            # n-1개의 원판을 목표 기둥으로 이동
            hanoi(n-1, via, end, start, result)

    result = []
    hanoi(n, 1, 3, 2, result)  # 시작 기둥 1, 목표 기둥 3, 중간 기둥 2
    return result