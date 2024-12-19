# 2week(0920)

### 강의 내용

<a href="https://velog.io/@davin0706/Ecole-%EC%BA%A1%EC%8A%A4%ED%86%A4-%EB%94%94%EC%9E%90%EC%9D%B8-2%EC%A3%BC%EC%B0%A8" target="_blank">
<img src="https://github.com/user-attachments/assets/c75e582c-adb8-4c77-90b4-eecf19404f1c" width="800"><br>
Click here to move!</a>

### La Piscine

<ul>
  <li>
    <b>1. 콜라츠 추측</b><br><br>
    <img src="https://github.com/user-attachments/assets/75242c51-824a-409b-a1f4-62dc84d78651" width="1000"><br><br>

    def solution(num):
    if num == 1:
        return 0
    
    cnt = 0
    
    while (num != 1):
        if (cnt == 500):
            return -1
        
        if (num % 2 == 0):
            num //= 2
        else:
            num = num*3 + 1
        cnt += 1
    
    return cnt
  </li>
  <li>
    <b>2. 하노이의 탑</b><br><br>
    <img src="https://github.com/user-attachments/assets/7aee0a7b-4d44-41be-9630-a26fedb640f8" width="1000"><br><br>

    def solution(n):
    def hanoi(n, start, end, via, result):
        if n == 1:
            # 원판을 시작 기둥에서 목표 기둥으로 이동
            result.append([start, end])
        else:
            # n-1개의 원판을 중간 기둥(via)로 이동
            hanoi(n-1, start, via, end, result)
            # 가장 큰 원판을 목표 기둥으로 이동
            result.append([start, end])
            # n-1개의 원판을 목표 기둥으로 이동
            hanoi(n-1, via, end, start, result)

    result = []
    hanoi(n, 1, 3, 2, result)  # 시작 기둥 1, 목표 기둥 3, 중간 기둥 2
    return result
  </li>
  <li>
    <b>3. 모음 사전</b><br><br>
    <img src="https://github.com/user-attachments/assets/a94c6c15-2d04-4c34-aba5-2b602897e03c" width="1000"><br><br>

    def solution(word):
    from itertools import product

    # 가능한 모든 단어 생성
    vowels = ['A', 'E', 'I', 'O', 'U']
    all_words = []

    for i in range(1, 6):  # 단어 길이: 1부터 5까지
        for p in product(vowels, repeat=i):
            all_words.append(''.join(p))

    # 사전 순 정렬
    all_words.sort()

    # 입력 단어의 위치 반환
    return all_words.index(word) + 1
  </li>
  <li>
    <b>4. 호텔 방 배정[통과 X]</b><br><br>
    <img src="https://github.com/user-attachments/assets/2f43dc54-565f-42ce-9716-a57b1a8edbd4" width="1000"><br><br>

    def solution(k, room_number):
    assigned = {}

    def find_next_empty(room):
        if room not in assigned:
            assigned[room] = room + 1
            return room
        assigned[room] = find_next_empty(assigned[room])
        return assigned[room]

    result = []
    for room in room_number:
        result.append(find_next_empty(room))

    return result
  </li>
  <li>
    <b>5. 모의고사</b><br><br>
    <img src="https://github.com/user-attachments/assets/30b2241c-e4d0-4897-8ee3-2b994e27701a" width="1000"><br><br>

    def solution(answers):
    # 각 수포자의 찍기 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # 각 수포자의 점수 계산
    scores = [0, 0, 0]
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1

    # 최고 점수를 받은 사람 찾기
    max_score = max(scores)
    return [i + 1 for i, score in enumerate(scores) if score == max_score]

  </li>
  <li>
    <b>6. 카펫</b><br><br>
    <img src="https://github.com/user-attachments/assets/fe51cc27-fff7-4f11-b00f-eea0864824c5" width="1000"><br><br>

    def solution(brown, yellow):
    width = 1

    while True:
        height = (brown+4 - 2*width) // 2
        if (width-2) * (height-2) == yellow:
            break
        width += 1
        
    return [max(width, height), min(width, height)]
  </li>
  <li>
    <b>7. 소수 찾기</b><br><br>
    <img src="https://github.com/user-attachments/assets/2b9c34b6-02eb-4518-a982-ccfdd1352066" width="1000"><br><br>

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
  </li>
  <li>
    <b>8. 불량 사용자</b><br><br>
    <img src="https://github.com/user-attachments/assets/2acd987b-34d4-49ee-918a-79af9705298d" width="1000"><br><br>

    from itertools import permutations

    def is_match(user, ban):
        if len(user) != len(ban):
            return False
        for u, b in zip(user, ban):
            if b != '*' and u != b:
                return False
        return True
    
    def solution(user_id, banned_id):
        possible = []
    
        # 모든 조합에서 밴 아이디와 매칭 여부 확인
        for perm in permutations(user_id, len(banned_id)):
            if all(is_match(perm[i], banned_id[i]) for i in range(len(banned_id))):
                perm_set = set(perm)
                if perm_set not in possible:
                    possible.append(perm_set)
    
        return len(possible)
  </li>
  <li>
    <b>9. 수식 최대화</b><br><br>
    <img src="https://github.com/user-attachments/assets/cb3af4b7-77ea-40a7-809b-53872161dfea" width="1000"><br><br>

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
  </li>
  <li>
    <b>10. 두 개 뽑아서 더하기</b><br><br>
    <img src="https://github.com/user-attachments/assets/e5baf88a-2b0d-42cc-a3a2-80b6b4c30105" width="1000"><br><br>

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
  </li>
  <li>
    <b>11. H-index</b><br><br>
    <img src="https://github.com/user-attachments/assets/221d856c-a758-401e-9207-2896616ad33c" width="1000"><br><br>

    def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] <= i+1:
            return max(citations[i], i)
        
    return len(citations) 
  </li>
  <li>
    <b>12. 문자열 내 마음대로 정렬하기</b><br><br>
    <img src="https://github.com/user-attachments/assets/3daa5cc3-e2b5-4134-912f-b944e11732a8" width="1000"><br><br>

    def solution(strings, n):
    # 정렬 기준: n번째 문자, 동일하면 전체 문자열 사전순
    return sorted(strings, key=lambda x: (x[n], x))
  </li>
  <li>
    <b>13. 가장 큰 수</b><br><br>
    <img src="https://github.com/user-attachments/assets/d8fec080-b049-449e-9193-60eb70b29eb4" width="1000"><br><br>

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
  </li>
  <li>
    <b>14. 입국심사</b><br><br>
    <img src="https://github.com/user-attachments/assets/28c1d511-92f1-47ec-a179-67c657297ce9" width="1000"><br><br>

    def solution(n, times):
    # 이진 탐색 범위 설정
    left, right = 1, max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2  # 중간 시간
        people = sum(mid // time for time in times)  # 처리 가능한 사람 수

        if people >= n:  # n명 이상 처리 가능
            answer = mid
            right = mid - 1
        else:  # 처리 불가
            left = mid + 1

    return answer
  </li>
  <li>
    <b>15. 순위 검색</b><br><br>
    <img src="https://github.com/user-attachments/assets/8baa9e5e-8945-4e22-b56a-fa2b90810502" width="1000"><br><br>

    from collections import defaultdict
    from itertools import combinations
    import bisect
    
    def solution(info, query):
        # 지원자 정보를 저장할 딕셔너리
        data = defaultdict(list)
    
        # 지원자 정보 처리
        for applicant in info:
            details = applicant.split()
            score = int(details[-1])
            conditions = details[:-1]
    
            # 모든 조합을 만들어 딕셔너리에 추가
            for r in range(5):
                for comb in combinations(range(4), r):
                    temp = ['-'] * 4
                    for idx in comb:
                        temp[idx] = conditions[idx]
                    data[''.join(temp)].append(score)
    
        # 딕셔너리 내 점수 리스트 정렬
        for key in data:
            data[key].sort()
    
        # 쿼리 처리
        result = []
        for q in query:
            details = q.replace(" and", "").split()
            key = ''.join(details[:-1])
            score = int(details[-1])
    
            # 해당 조건의 지원자 점수 리스트
            scores = data.get(key, [])
    
            # 이진 탐색으로 점수 조건 만족하는 개수 찾기
            index = bisect.bisect_left(scores, score)
            result.append(len(scores) - index)
    
        return result
  </li>
</ul>
