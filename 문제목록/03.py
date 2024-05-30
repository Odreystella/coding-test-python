'''
문제 03 두 개 뽑아서 더하기

난이도: ⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(N²log(N²))
출제: 프로그래머스
정답률: 68%

제약조건:
    - numbers 길이는 2 이상 100 이하입니다.
    - numbers의 모든 수는 0이상 100 이하입니다. 

입출력의 예: 입력 -> 출력
    - [2, 1, 3, 4, 1] -> [2, 3, 4, 5, 6, 7]
    - [5, 0, 2, 7] -> [2, 5, 7, 9, 12]
'''


# 정수 배열을 하나 받고, 서로 다른 인덱스에 있는 2개의 수를 뽑아 더해 만들 수 있는 모든 수를
# 배열에 오름차순으로 담아 반환하는 solution() 함수를 완성하세요.
def solution(numbers):
    answer = []
    for i in numbers:
        idx = numbers.index(i) # O(N)
        for j in numbers[idx+1:]:
            answer.append(i+j) # 이중 for문 O(N²)
    result = list(set(answer)) # O(N)
    result.sort() # O(NlogN)
    return result


# 다른 사람 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(set(answer))


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([2, 1, 3, 4, 1])) # 반환값 : [2, 3, 4, 5, 6, 7]
# print(solution([5, 0, 2, 7])) # 반환값 : [2, 5, 7, 9, 12]


'''
Note:
- 정수 길이가 100이하니까 시간 복잡도 고려하지 않고, 이중으로 반복문 돌기 O(N²)
- 다른 사람 풀이 보니 range()쓰면 나처럼 인덱스 구하는 코드가 없어도 됨
- 최종 시간복잡도는 O(N²)
''' 
