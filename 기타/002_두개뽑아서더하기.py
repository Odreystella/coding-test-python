"""
문제: 두 개 뽑아서 더하기

난이도: Lv.1
출제: 프로그래머스 스킬체크 레벨 1
정답률: 71%
날짜: 2024-07-01 월요일
"""


def solution(numbers):
    answer = []
    for i in range(len(numbers)): # O(N^2)
        for j in range(i+1, len(numbers)):
            result = numbers[i] + numbers[j] # O(1)
            answer.append(result) #O(1)
    return sorted(list(set(answer))) # O(N)


"""
Note:
- 배열의 크기: 10^2 시간복잡도 신경 안써도 됨
- 길이 만큼의 두개의 수를 뽑는 모든 경우의 수를 완전탐색으로 구하고
- 그 값들을 더해서 answer에 저장한 다음
- 중복값이 있을 수 있으니 set해서 오름차순으로 리턴
"""
