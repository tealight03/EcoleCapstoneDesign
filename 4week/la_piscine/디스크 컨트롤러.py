import heapq

def solution(jobs):
    jobs.sort()  # 요청 시간 순으로 정렬
    heap = []
    time = 0  # 현재 시간
    index = 0  # jobs의 인덱스
    total_time = 0  # 요청부터 종료까지의 총 시간 합

    while index < len(jobs) or heap:
        # 현재 시간까지 요청된 작업을 힙에 추가
        while index < len(jobs) and jobs[index][0] <= time:
            heapq.heappush(heap, (jobs[index][1], jobs[index][0]))  # (소요 시간, 요청 시간)
            index += 1

        if heap:
            # 소요 시간이 가장 짧은 작업을 처리
            duration, request_time = heapq.heappop(heap)
            time += duration
            total_time += time - request_time
        else:
            # 힙이 비어 있으면 다음 작업의 요청 시간으로 점프
            time = jobs[index][0]

    return total_time // len(jobs)