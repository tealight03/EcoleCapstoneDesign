# 3week(1004)

### 강의 내용
<a href="https://velog.io/@davin0706/Ecole-%EC%BA%A1%EC%8A%A4%ED%86%A4-%EB%94%94%EC%9E%90%EC%9D%B8-3%EC%A3%BC%EC%B0%A8" target="_blank">
<img src="https://github.com/user-attachments/assets/2cd9977d-04ae-469c-8bf7-3593516e05b2" width="800"><br>
Click here to move!</a>

### La Piscine
<ul>
  <li>
    <b>1. 징검다리</b><br><br>
    <img src="https://github.com/user-attachments/assets/ddb31879-0d59-4d38-ad41-ce075fcd811d" width="1000"><br><br>

    def solution(distance, rocks, n):
    # 바위 위치를 정렬하고, 도착점을 추가
    rocks.sort()
    rocks.append(distance)

    # 이진 탐색의 범위를 정의
    left, right = 0, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 현재 최소 거리 설정
        prev = 0  # 이전 위치
        removed = 0  # 제거한 바위 개수

        for rock in rocks:
            if rock - prev < mid:
                # 최소 거리 조건을 만족하지 않으면 바위 제거
                removed += 1
            else:
                # 조건을 만족하면 이전 위치를 현재 바위로 갱신
                prev = rock

        if removed > n:
            # 제거한 바위가 너무 많으면 거리 줄이기
            right = mid - 1
        else:
            # 조건을 만족하면 거리 늘리기
            answer = mid  # 현재 거리 저장
            left = mid + 1

    return answer
  </li>
  <li>
    <b>2. 징검다리 건너기</b><br><br>
    <img src="https://github.com/user-attachments/assets/c429b2c5-d084-42b6-b5cd-3248ad37f96b" width="1000"><br><br>

    def solution(stones, k):
    # 이진 탐색을 위한 최소값과 최대값 설정
    left, right = 1, max(stones)

    while left <= right:
        mid = (left + right) // 2  # 건널 수 있는 친구들의 수의 중간값
        consecutive_zeros = 0  # 연속된 0의 개수 초기화

        for stone in stones:
            if stone < mid:
                consecutive_zeros += 1
                if consecutive_zeros >= k:
                    break
            else:
                consecutive_zeros = 0

        if consecutive_zeros >= k:
            # 건널 수 없는 경우 -> 친구 수를 줄인다
            right = mid - 1
        else:
            # 건널 수 있는 경우 -> 친구 수를 늘린다
            left = mid + 1

    return right
  </li>
  <li>
    <b>3. 완주하지 못한 선수</b><br><br>
    <img src="https://github.com/user-attachments/assets/b60ea560-5cee-49e4-8b31-f4b1a42c8aeb" width="1000"><br><br>

    from collections import Counter

    def solution(participant, completion):
        # 참가자와 완주자 이름의 카운트를 계산
        participant_count = Counter(participant)
        completion_count = Counter(completion)
    
        # 차이를 계산하여 완주하지 못한 사람을 찾음
        for person in participant_count:
            if participant_count[person] != completion_count[person]:
                return person
  </li>
  <li>
    <b>4. 전화번호 목록</b><br><br>
    <img src="https://github.com/user-attachments/assets/b7b4573d-0726-4683-a778-fd9cfc9289d3" width="1000"><br><br>

    def solution(phone_book):
    # 전화번호부를 정렬
    phone_book.sort()

    # 인접한 두 번호를 비교
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True
  </li>
  <li>
    <b>5. 의상</b><br><br>
    <img src="https://github.com/user-attachments/assets/f0d7f041-a069-44f2-876e-b195cb86778f" width="1000"><br><br>

    from collections import Counter

    def solution(clothes):
        # 각 의상의 종류별로 개수를 세기
        clothes_count = Counter([kind for name, kind in clothes])
    
        # 조합 계산: (각 종류의 개수 + 1)을 모두 곱한 뒤, -1 (아무것도 입지 않은 경우 제외)
        combinations = 1
        for count in clothes_count.values():
            combinations *= (count + 1)
    
        return combinations - 1
  </li>
  <li>
    <b>6. 오픈채팅방</b><br><br>
    <img src="https://github.com/user-attachments/assets/fa8cc901-125a-41cb-b34c-d7c8adf40b03" width="1000"><br><br>

    def solution(record):
    dict = {}
    log = []
    record = [inst.split(' ') for inst in record]

    for inst in record :
        if (inst[0] == 'Enter') or (inst[0] == 'Change') :
            dict[inst[1]] = inst[2]

    for inst in record :
        if inst[0] == 'Enter' :
            log.append('%s님이 들어왔습니다.'%dict[inst[1]])
        elif inst[0] == 'Leave' :
            log.append('%s님이 나갔습니다.'%dict[inst[1]])

    return log
  </li>
  <li>
    <b>7. 베스트앨범</b><br><br>
    <img src="https://github.com/user-attachments/assets/0bdfac8f-b4b8-4cf1-9e9a-f3b16db3e9bb" width="1000"><br><br>

    from collections import defaultdict

    def solution(genres, plays):
        # 장르별 총 재생 횟수와 곡별 재생 횟수를 저장
        genre_play_count = defaultdict(int)
        songs = defaultdict(list)
    
        for i, (genre, play) in enumerate(zip(genres, plays)):
            genre_play_count[genre] += play
            songs[genre].append((play, i))
    
        # 장르별로 정렬
        sorted_genres = sorted(genre_play_count.keys(), key=lambda x: genre_play_count[x], reverse=True)
    
        answer = []
        for genre in sorted_genres:
            # 각 장르에서 곡을 재생 횟수와 고유 번호로 정렬 (내림차순, 고유 번호는 오름차순)
            sorted_songs = sorted(songs[genre], key=lambda x: (-x[0], x[1]))
            # 상위 두 곡을 추가
            answer.extend([idx for _, idx in sorted_songs[:2]])
    
        return answer
  </li>
  <li>
    <b>8. 피보나치 수</b><br><br>
    <img src="https://github.com/user-attachments/assets/8ca87ee3-25e8-46a2-8620-ae9fab820751" width="1000"><br><br>

    def solution(n):
    fibo = [0, 1, 1]
    
    if n == 0 or n == 1 or n == 2:
        return fibo[n]
    
    for i in range(3, n+1):
        fibo.append(fibo[i-2] + fibo[i-1])
    
    return fibo[n] % 1234567
  </li>
  <li>
    <b>9. N으로 표현</b><br><br>
    <img src="https://github.com/user-attachments/assets/433815c0-6f2f-41ca-955b-64260f667992" width="1000"><br><br>

    def solution(N, number):
    # 동적 계획법을 위한 집합 리스트 초기화
    dp = [set() for _ in range(9)]  # N을 1번 사용한 경우부터 8번 사용한 경우까지

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N을 i번 반복한 수 (예: 5, 55, 555, ...)

        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        if number in dp[i]:
            return i

    return -1
  </li>
  <li>
    <b>10. 정수 삼각형</b><br><br>
    <img src="https://github.com/user-attachments/assets/102399f5-acaf-46b8-9eba-43186fc84995" width="1000"><br><br>

    def solution(triangle):
    # 아래에서부터 위로 합산
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 현재 위치에 아래층에서 가능한 최대 값을 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]
  </li>
  <li>
    <b>11. 등굣길</b><br><br>
    <img src="https://github.com/user-attachments/assets/ab186b83-2eeb-4772-bddd-3a012917cc4b" width="1000"><br><br>

    def solution(m, n, puddles):
    # 2D DP 테이블 초기화
    dp = [[0] * m for _ in range(n)]

    # 시작점 초기화
    dp[0][0] = 1

    # 웅덩이를 1로 표시해 계산 제외
    for x, y in puddles:
        dp[y - 1][x - 1] = -1

    # DP 테이블 채우기
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                dp[i][j] = 0  # 웅덩이는 경로가 0개
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]  # 위쪽에서 오는 경로
                if j > 0:
                    dp[i][j] += dp[i][j - 1]  # 왼쪽에서 오는 경로

                dp[i][j] %= 1000000007

    return dp[n - 1][m - 1]
  </li>
  <li>
    <b>12. 도둑질</b><br><br>
    <img src="https://github.com/user-attachments/assets/e59b137d-9a49-49a3-9672-b72acc3272b6" width="1000"><br><br>

    def solution(money):
    n = len(money)

    # 첫 번째 집을 털 경우
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, n - 1):  # 마지막 집은 털지 않음
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫 번째 집을 털지 않을 경우
    dp2 = [0] * n
    dp2[1] = money[1]

    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[n - 2], dp2[n - 1])
  </li>
  <li>
    <b>13. 주식가격</b><br><br>
    <img src="https://github.com/user-attachments/assets/d0ba9094-cfd6-4a2c-883e-c1352e089f4c" width="1000"><br><br>

    def solution(prices):
    n = len(prices)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer
  </li>
  <li>
    <b>14. 기능개발</b><br><br>
    <img src="https://github.com/user-attachments/assets/d29d3af2-b3a1-4fab-8d26-55b79876f9d7" width="1000"><br><br>

    import math

    def solution(progresses, speeds):
        answer = []
        days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]  # 각 작업의 소요 시간 계산
    
        while days:
            current = days.pop(0)  # 첫 번째 작업의 배포 시간
            count = 1
    
            # 현재 작업과 함께 배포될 작업 계산
            while days and days[0] <= current:
                days.pop(0)
                count += 1
    
            answer.append(count)
    
        return answer
  </li>
  <li>
    <b>15. 가장 먼 노드</b><br><br>
    <img src="https://github.com/user-attachments/assets/9bd8903d-112c-4c25-9a30-b5053a4ca807" width="1000"><br><br>
    
    from collections import deque, defaultdict

    def solution(n, edge):
        # 그래프 초기화
        graph = defaultdict(list)
        for a, b in edge:
            graph[a].append(b)
            graph[b].append(a)
    
        # BFS로 최단 거리 계산
        distances = [-1] * (n + 1)
        distances[1] = 0  # 시작 노드
        queue = deque([1])
    
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if distances[neighbor] == -1:  # 방문하지 않은 노드만
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
    
        # 가장 먼 거리의 노드 개수 계산
        max_distance = max(distances)
        return distances.count(max_distance)
  </li>
</ul>
