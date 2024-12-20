def solution(stones, k):
    # 이진 탐색을 위한 최소값과 최대값 설정
    left, right = 1, max(stones)

    while left <= right:
        mid = (left + right) // 2  # 건널 수 있는 친구들의 수의 중간값
        consecutive_zeros = 0  # 연속된 0의 개수 초기화

        for stone in stones:
            if stone < mid:
                consecutive_zeros += 1
                if consecutive_zeros >= k:
                    break
            else:
                consecutive_zeros = 0

        if consecutive_zeros >= k:
            # 건널 수 없는 경우 -> 친구 수를 줄인다
            right = mid - 1
        else:
            # 건널 수 있는 경우 -> 친구 수를 늘린다
            left = mid + 1

    return right