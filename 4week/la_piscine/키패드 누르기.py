def solution(numbers, hand):
    # 키패드 위치 정의
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    # 현재 위치 초기화
    left_pos = keypad['*']
    right_pos = keypad['#']

    result = []

    for number in numbers:
        if number in [1, 4, 7]:
            result.append('L')
            left_pos = keypad[number]
        elif number in [3, 6, 9]:
            result.append('R')
            right_pos = keypad[number]
        else:
            # 거리 계산
            target_pos = keypad[number]
            left_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            right_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])

            if left_dist < right_dist:
                result.append('L')
                left_pos = target_pos
            elif right_dist < left_dist:
                result.append('R')
                right_pos = target_pos
            else:
                if hand == "right":
                    result.append('R')
                    right_pos = target_pos
                else:
                    result.append('L')
                    left_pos = target_pos

    return ''.join(result)