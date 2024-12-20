def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0

        # 현재 숫자를 더하거나 빼는 두 가지 선택
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

    return dfs(0, 0)