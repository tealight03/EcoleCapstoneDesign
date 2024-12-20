def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_order = list(skill)

        for s in skill_tree:
            if s in skill_order:
                if s == skill_order[0]:
                    skill_order.pop(0)  # 올바른 순서대로 배우면 제거
                else:
                    break  # 순서가 맞지 않으면 중단
        else:
            # 정상적으로 모든 문자를 확인한 경우
            answer += 1

    return answer