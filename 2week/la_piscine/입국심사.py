def solution(n, times):
    # 이진 탐색 범위 설정
    left, right = 1, max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2  # 중간 시간
        people = sum(mid // time for time in times)  # 처리 가능한 사람 수

        if people >= n:  # n명 이상 처리 가능
            answer = mid
            right = mid - 1
        else:  # 처리 불가
            left = mid + 1

    return answer