from collections import Counter

def solution(participant, completion):
    # 참가자와 완주자 이름의 카운트를 계산
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    # 차이를 계산하여 완주하지 못한 사람을 찾음
    for person in participant_count:
        if participant_count[person] != completion_count[person]:
            return person