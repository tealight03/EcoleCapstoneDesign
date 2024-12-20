def solution(n):
    fibo = [0, 1, 1]
    
    if n == 0 or n == 1 or n == 2:
        return fibo[n]
    
    for i in range(3, n+1):
        fibo.append(fibo[i-2] + fibo[i-1])
    
    return fibo[n] % 1234567