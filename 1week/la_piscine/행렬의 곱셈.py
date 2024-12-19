def solution(arr1, arr2):
    ans = [] # 결과 행렬을 담을 리스트
    
    # arr1 행렬의 각 행에 대해 반복
    for i in range(len(arr1)):
        res = [] # 새 행렬의 한 행을 임시로 저장할 리스트
        
        # arr2 행렬의 열에 대해 반복복
        for j in range(len(arr2[0])):
            tmp = 0 # 한 원소에 대한 계산을 임시 저장할 변수수
            
            # arr1 행렬의 열과 arr2 행렬의 행에 대해 곱셈 연산 수행행
            for k in range(len(arr1[0])):
                tmp += arr1[i][k] * arr2[k][j]
                
            res.append(tmp) # 계산된 값을 현재 행에 추가
        ans.append(res) # 완성된 행을 결과 행렬에 추가가
    
    return ans # 최종 결과 행렬 반환