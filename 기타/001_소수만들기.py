"""
문제: 소수만들기

난이도: Lv.1
출제: 프로그래머스 스킬체크 레벨 1
정답률: 63%
날짜: 2024-07-01 월요일
"""


def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum_nums = nums[i]+nums[j]+nums[k]
                result = is_prime_number(sum_nums)
                if result:
                    answer += 1
    return answer


"""
Note:
- 배열의 길이는 3개 이상 50 이하, 시간복잡도 신경 안써도 됨
- 숫자 3개를 뽑는 경우의 수를 모두 구하고, 각 값들이 소수인지 아닌지 확인 할 때 answer에 +1
- 1과 자기 자신만 있는 경우가 소수
"""

