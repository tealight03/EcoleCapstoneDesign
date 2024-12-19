def solution(s, n):
    def shift_char(c, n):
        if c.islower():  # 소문자
            return chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        elif c.isupper():  # 대문자
            return chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        else:
            return c  # 공백 등은 그대로 반환

    # 문자열의 각 문자에 대해 시저 암호 적용
    return ''.join(shift_char(c, n) for c in s)