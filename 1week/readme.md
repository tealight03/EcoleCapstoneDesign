# 1week(0907)

### 강의 내용

<a href="https://velog.io/@davin0706/Ecole-%EC%BA%A1%EC%8A%A4%ED%86%A4-%EB%94%94%EC%9E%90%EC%9D%B8-1%EC%A3%BC%EC%B0%A8" target="_blank">
<img src="https://github.com/user-attachments/assets/cb1e20ab-0c40-492c-97eb-7aca11a56260" width="800"><br>
Click here to move!</a>

### La Piscine

<ul>
  <li>
    <b>1. 교점에 별 만들기</b><br><br>
    <img src="https://github.com/user-attachments/assets/784e4d8a-e504-4f29-bb74-377247ab767b" width="1000"><br><br>
    
    def solution(line):
        import math
    
        # 교점 좌표를 저장할 리스트
        points = []
    
        # 직선끼리 교점 구하기
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                A, B, E = line[i]
                C, D, F = line[j]
    
                # 교점이 존재하는 조건: AD - BC != 0
                denominator = A * D - B * C
                if denominator == 0:
                    continue
    
                # x, y 좌표 계산
                x = (B * F - E * D) / denominator
                y = (E * C - A * F) / denominator
    
                # 정수 좌표만 고려
                if x == int(x) and y == int(y):
                    points.append((int(x), int(y)))
    
        # 교점 중 최대, 최소값 구하기
        min_x = min(points, key=lambda p: p[0])[0]
        max_x = max(points, key=lambda p: p[0])[0]
        min_y = min(points, key=lambda p: p[1])[1]
        max_y = max(points, key=lambda p: p[1])[1]
    
        # 격자 크기 계산
        width = max_x - min_x + 1
        height = max_y - min_y + 1
    
        # 격자 초기화
        grid = [['.'] * width for _ in range(height)]
    
        # 교점 위치 표시
        for x, y in points:
            grid[max_y - y][x - min_x] = '*'
    
        # 격자를 문자열로 변환하여 반환
        return [''.join(row) for row in grid]
    
    # 테스트 실행
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    result = solution(line)
    for row in result:
        print(row)
  </li>
  <li>
    <b>2. 행렬 테두리 회전하기</b><br><br>
    <img src="https://github.com/user-attachments/assets/7af253c2-669b-45aa-ba36-9bd846c1f8a2" width="1000"><br><br>
    
      def solution(rows, columns, queries):
      # 초기 행렬 생성
      matrix = [[(i * columns) + j + 1 for j in range(columns)] for i in range(rows)]
  
      # 결과를 저장할 리스트
      answer = []
  
      # 회전 처리
      for query in queries:
          x1, y1, x2, y2 = [q - 1 for q in query]  # 0-index로 변환
          temp = matrix[x1][y1]  # 첫 번째 값을 임시 저장
          min_value = temp
  
          # 왼쪽 세로 이동
          for i in range(x1, x2):
              matrix[i][y1] = matrix[i + 1][y1]
              min_value = min(min_value, matrix[i][y1])
  
          # 아래쪽 가로 이동
          for i in range(y1, y2):
              matrix[x2][i] = matrix[x2][i + 1]
              min_value = min(min_value, matrix[x2][i])
  
          # 오른쪽 세로 이동
          for i in range(x2, x1, -1):
              matrix[i][y2] = matrix[i - 1][y2]
              min_value = min(min_value, matrix[i][y2])
  
          # 위쪽 가로 이동
          for i in range(y2, y1, -1):
              matrix[x1][i] = matrix[x1][i - 1]
              min_value = min(min_value, matrix[x1][i])
  
          # 마지막 값 복원
          matrix[x1][y1 + 1] = temp
  
          # 최솟값 저장
          answer.append(min_value)
  
      return answer
  </li>
  <li>
    <b>3. 삼각 달팽이</b><br><br>
    <img src="https://github.com/user-attachments/assets/cb73e62f-4a0f-4aec-94f6-c50a67c29c11" width="1000"><br><br>

    def solution(n):
    # 삼각형 배열 초기화
    triangle = [[0] * i for i in range(1, n + 1)]

    # 방향 설정 (아래, 오른쪽, 왼쪽 위 대각선)
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    x, y = 0, 0  # 시작 위치
    direction = 0  # 초기 방향 (아래)
    num = 1  # 삼각형에 채울 숫자

    while num <= n * (n + 1) // 2:  # 채워야 할 숫자의 범위
        triangle[x][y] = num
        num += 1

        # 다음 위치 계산
        nx, ny = x + dx[direction], y + dy[direction]

        # 범위를 벗어나거나 이미 숫자가 채워져 있는 경우 방향 전환
        if nx < 0 or ny < 0 or nx >= n or ny >= len(triangle[nx]) or triangle[nx][ny] != 0:
            direction = (direction + 1) % 3
            nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny

    # 결과를 일차원 리스트로 변환하여 반환
    result = []
    for row in triangle:
        result.extend(row)

    return result
  </li>
  <li>
    <b>4. 거리두기 확인하기</b><br><br>
    <img src="https://github.com/user-attachments/assets/702f157c-07b7-46d3-b34c-ec973c4b478b" width="1000"><br><br>

    def solution(places):
    from collections import deque

    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def is_valid(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':  # 사람이 있는 경우
                    if not bfs(i, j, place):
                        return 0
        return 1

    def bfs(x, y, place):
        queue = deque([(x, y, 0)])  # (x, y, 거리)
        visited = [[False] * 5 for _ in range(5)]
        visited[x][y] = True

        while queue:
            cx, cy, dist = queue.popleft()

            if dist > 0 and place[cx][cy] == 'P':  # 거리 안에 사람이 있는 경우
                return False

            if dist >= 2:  # 거리 2를 넘으면 검사 중단
                continue

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if place[nx][ny] != 'X':  # 파티션이 아닌 경우만 이동
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))

        return True

    return [is_valid(place) for place in places]
  </li>
  <li>
    <b>5. 행렬의 곱셈</b><br><br>
    <img src="https://github.com/user-attachments/assets/1cc513c6-faf9-49bd-b646-4255c5bd8eea" width="1000"><br><br>
    
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
  </li>
  <li>
    <b>6. 시저 암호</b><br><br>
    <img src="https://github.com/user-attachments/assets/f7a5a5e3-7192-4f3b-891e-d297ee318792" width="1000"><br><br>

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
  </li>
  <li>
    <b>7. 이상한 문자 만들기</b><br><br>
    <img src="https://github.com/user-attachments/assets/3be8d8e2-1b74-40d9-aa38-a50b55c71e2a" width="1000"><br><br>

    def solution(s):
    def convert_word(word):
        # 각 단어를 변환: 짝수 인덱스 -> 대문자, 홀수 인덱스 -> 소문자
        return ''.join(
            c.upper() if i % 2 == 0 else c.lower()
            for i, c in enumerate(word)
        )

    # 문자열을 단어별로 나누어 변환 후 다시 합치기
    return ' '.join(convert_word(word) for word in s.split(' '))
  </li>
  <li>
    <b>8. 튜플</b><br><br>
    <img src="https://github.com/user-attachments/assets/d97c6ebb-3608-4669-ad37-54b4e732fee8" width="1000"><br><br>

    def solution(s):
    answer = []
    s = s[:-2].replace('{','').replace(',',' ').split('}')
    
    s = [i.split() for i in s]
    
    s.sort(key=lambda x:len(x))

    for tup in s:
        for i in answer:
            tup.remove(i)
        answer.append(tup[0])
    
    answer = [int(i) for i in answer]
    
    return answer
  </li>
  <li>
    <b>9. 짝지어 제거하기</b><br><br>
    <img src="https://github.com/user-attachments/assets/7b05d6e3-d770-4bc3-bd34-427c7da6dbaa" width="1000"><br><br>

    def solution(s):
    stack = []
    
    for ch in s :
        if stack and stack[-1] == ch:
            stack.pop()
            continue
        
        stack.append(ch)
    
    return 1 if not stack else 0
  </li>
  <li>
    <b>10. 문자열 압축</b><br><br>
    <img src="https://github.com/user-attachments/assets/4ec4e96c-9d47-40af-b45d-8b1f0e12a9d1" width="1000"><br><br>

    def solution(s):
    def compress(length):
        compressed = ""
        count = 1
        prev = s[:length]

        for i in range(length, len(s), length):
            current = s[i:i + length]
            if prev == current:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = current
                count = 1

        compressed += (str(count) + prev) if count > 1 else prev
        return len(compressed)

    if len(s) == 1:
        return 1

    return min(compress(length) for length in range(1, len(s) // 2 + 1))
  </li>
  <li>
    <b>11. 3진법 뒤집기</b><br><br>
    <img src="https://github.com/user-attachments/assets/b1cc8498-0876-4ccd-a76b-98d5ce4c931c" width="1000"><br><br>

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
  </li>
  <li>
    <b>12. 이진 변환 반복하기</b><br><br>
    <img src="https://github.com/user-attachments/assets/539d950e-3764-4bb7-92d4-919677c409a1" width="1000"><br><br>

    def solution(s):
    binary_conversion_count = 0
    removed_zero_count = 0

    while s != "1":
        # 0 제거
        removed_zero_count += s.count("0")
        s = s.replace("0", "")

        # 길이를 2진수로 변환
        s = bin(len(s))[2:]
        binary_conversion_count += 1

    return [binary_conversion_count, removed_zero_count]
  </li>
  <li>
    <b>13. 신규 아이디 추천</b><br><br>
    <img src="https://github.com/user-attachments/assets/f1f0e0e4-3301-4b70-b83b-ac7730b2eb92" width="1000"><br><br>

    import re

    def solution(new_id):
        # 1단계: 모든 대문자를 소문자로 치환
        new_id = new_id.lower()
    
        # 2단계: 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
        new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)
    
        # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환
        new_id = re.sub(r"\.+", ".", new_id)
    
        # 4단계: 마침표(.)가 처음이나 끝에 위치하면 제거
        new_id = new_id.strip(".")
    
        # 5단계: 빈 문자열이라면 "a"를 대입
        if not new_id:
            new_id = "a"
    
        # 6단계: 길이가 16자 이상이면 첫 15개 문자를 제외한 나머지 제거
        #        제거 후 마침표(.)가 끝에 위치하면 제거
        if len(new_id) >= 16:
            new_id = new_id[:15].rstrip(".")
    
        # 7단계: 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복
        while len(new_id) < 3:
            new_id += new_id[-1]
    
        return new_id
  </li>
  <li>
    <b>14. 문자열 다루기 기본</b><br><br>
    <img src="https://github.com/user-attachments/assets/8ab1d99c-01b9-4325-9e37-3a306115276c" width="1000"><br><br>

    def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isnumeric()
    else:
        return False
  </li>
  <li>
    <b>15. 핸드폰 번호 가리기</b><br><br>
    <img src="https://github.com/user-attachments/assets/a0085c67-253b-4930-b7b4-225beb43c3cb" width="1000"><br><br>
    
    def solution(phone_number):
    # 전화번호의 뒤 4자리를 제외한 나머지를 *로 대체
    return "*" * (len(phone_number) - 4) + phone_number[-4:]
  </li>
</ul>
