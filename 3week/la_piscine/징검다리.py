def solution(distance, rocks, n):
    # 바위 위치를 정렬하고, 도착점을 추가
    rocks.sort()
    rocks.append(distance)

    # 이진 탐색의 범위를 정의
    left, right = 0, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 현재 최소 거리 설정
        prev = 0  # 이전 위치
        removed = 0  # 제거한 바위 개수

        for rock in rocks:
            if rock - prev < mid:
                # 최소 거리 조건을 만족하지 않으면 바위 제거
                removed += 1
            else:
                # 조건을 만족하면 이전 위치를 현재 바위로 갱신
                prev = rock

        if removed > n:
            # 제거한 바위가 너무 많으면 거리 줄이기
            right = mid - 1
        else:
            # 조건을 만족하면 거리 늘리기
            answer = mid  # 현재 거리 저장
            left = mid + 1

    return answer