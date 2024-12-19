from itertools import permutations

def solution(expression):
    # 가능한 연산자 우선순위
    operators = ['+', '-', '*']
    operator_orders = list(permutations(operators))

    # 계산 함수
    def calculate(expression, operator_order):
        exp = expression[:]
        for op in operator_order:
            stack = []
            while exp:
                token = exp.pop(0)
                if token == op:
                    stack.append(str(eval(stack.pop() + op + exp.pop(0))))
                else:
                    stack.append(token)
            exp = stack
        return abs(int(exp[0]))

    # 토큰화
    import re
    tokens = re.split(r'(\D)', expression)  # 숫자와 연산자를 분리

    # 각 우선순위에 따른 계산 결과의 최댓값
    max_result = 0
    for order in operator_orders:
        max_result = max(max_result, calculate(tokens[:], order))

    return max_result