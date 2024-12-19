def triple_decimal (x):
    if x == 0:
        return '0'
    digits = []
    
    while x:
        digits.append(str(x % 3))
        x //= 3
    return ''.join(digits[::-1])

def solution(n):
    answer = 0
    
    change = triple_decimal(n)
    
    for i in range(len(change)):
        answer += int(change[i]) * (3**i)
    
    return answer