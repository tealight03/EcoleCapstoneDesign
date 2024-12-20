import math

def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))  # 1부터 n까지의 숫자 리스트
    k -= 1  # 인덱스 보정을 위해 k를 0-based로 변환

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)  # (i-1)! 계산
        index = k // fact  # 현재 자릿수에 해당하는 숫자의 인덱스
        answer.append(numbers.pop(index))  # 해당 숫자를 결과에 추가
        k %= fact  # 남은 순열 인덱스 갱신

    return answer
