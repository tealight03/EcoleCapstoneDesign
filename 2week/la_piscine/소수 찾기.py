from itertools import permutations

def solution(numbers):
    # 가능한 모든 숫자 조합 생성
    possible_numbers = set()
    for i in range(1, len(numbers) + 1):
        for combo in permutations(numbers, i):
            possible_numbers.add(int(''.join(combo)))

    # 소수 판별 함수
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # 소수 개수 세기
    return sum(1 for number in possible_numbers if is_prime(number))