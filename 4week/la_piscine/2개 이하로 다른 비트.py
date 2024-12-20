def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            # 짝수인 경우, +1 하면 비트가 하나만 달라짐
            answer.append(number + 1)
        else:
            # 홀수인 경우, 가장 오른쪽에서 처음 등장하는 0을 1로 바꾸고
            # 그 다음 비트를 0으로 바꾼다
            binary = list('0' + bin(number)[2:])  # 앞에 '0' 추가
            for i in range(len(binary) - 1, -1, -1):
                if binary[i] == '0':
                    binary[i] = '1'
                    binary[i + 1] = '0'
                    break
            answer.append(int(''.join(binary), 2))

    return answer