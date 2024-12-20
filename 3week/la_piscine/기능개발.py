import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]  # 각 작업의 소요 시간 계산

    while days:
        current = days.pop(0)  # 첫 번째 작업의 배포 시간
        count = 1

        # 현재 작업과 함께 배포될 작업 계산
        while days and days[0] <= current:
            days.pop(0)
            count += 1

        answer.append(count)

    return answer