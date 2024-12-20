def solution(p):
    # 균형잡힌 괄호 문자열 분리
    def split_balanced(s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                return s[:i + 1], s[i + 1:]

    # 올바른 괄호 문자열 확인
    def is_correct(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    # 변환 함수
    def transform(s):
        if not s:
            return ""
        u, v = split_balanced(s)
        if is_correct(u):
            return u + transform(v)
        else:
            return '(' + transform(v) + ')' + ''.join('(' if c == ')' else ')' for c in u[1:-1])

    return transform(p)