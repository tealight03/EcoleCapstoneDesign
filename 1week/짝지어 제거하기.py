def solution(s):
    stack = []
    
    for ch in s :
        if stack and stack[-1] == ch:
            stack.pop()
            continue
        
        stack.append(ch)
    
    return 1 if not stack else 0