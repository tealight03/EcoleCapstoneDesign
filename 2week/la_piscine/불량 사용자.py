from itertools import permutations

def is_match(user, ban):
    if len(user) != len(ban):
        return False
    for u, b in zip(user, ban):
        if b != '*' and u != b:
            return False
    return True

def solution(user_id, banned_id):
    possible = []

    # 모든 조합에서 밴 아이디와 매칭 여부 확인
    for perm in permutations(user_id, len(banned_id)):
        if all(is_match(perm[i], banned_id[i]) for i in range(len(banned_id))):
            perm_set = set(perm)
            if perm_set not in possible:
                possible.append(perm_set)

    return len(possible)