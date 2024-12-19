def solution(numbers):
    arr = []
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if (numbers[i]+numbers[j]) not in arr:
                arr.append(numbers[i]+numbers[j])
                
    arr = sorted(arr)
    
    return arr