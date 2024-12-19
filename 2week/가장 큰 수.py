def solution(numbers):
    ans = str()
    
    # 입력된 리스트의 모든 원소를 문자열로 변환
    numbers = [str(x) for x in numbers]
    
    # 입력된 리스트의 모든 원소가 0인 경우 0을 출력하도록 별도로 처리
    if all(num == '0' for num in numbers):
        return "0"
    
    # 그 외 경우
    else:
        # 문자열을 3번 더해서 사전 순서로 문자열을 비교해준다
        # 이때 문자열은 한 문자씩 잘라서 비교하기 때문에
        # 우리가 원하는대로 한 자리씩 자릿수를 비교하게 된다
        # 참고로, 한 문자열의 끝까지 비교했을 때
        # 자릿수가 계속 동일했다면 길이가 더 짧은 문자열이 먼저 오도록 정렬한다
        numbers.sort(key=lambda x: (x*3), reverse=True)
        
        # 정렬한 문자열을 순서대로 병합한다
        for s in numbers:
            ans += s

        return ans