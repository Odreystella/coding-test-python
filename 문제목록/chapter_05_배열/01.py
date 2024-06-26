'''
문제 01 배열 정렬하기 

난이도: ⭐️
저자 권장 시간: 10분
권장 시간 복잡도: O(NlogN)
출제: 저자 출제
날짜: 2024-05-24 금요일

제약조건:
    - 정수 배열의 길이는 2 이상 10⁵ 이하입니다.
    - 정수 배열의 각 데이터 값은 -100,000 이상 100,000 이하 입니다.

입출력의 예: 입력 -> 출력
    - [1, -5, 2, 4, 3] -> [-5, 1, 2, 3, 4]
    - [2, 1, 1, 3, 2, 5, 4] -> [1, 1, 2, 2, 3, 4, 5]
    - [6, 1, 7] -> [1, 6, 7]
'''


# 정수 배열을 정렬해서 반환하는 solution() 함수를 완성하세요.
def solution(arr):
    arr.sort()  # O(NlogN)
    return arr


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
# print(solution([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
# print(solution([1,6,7])) # 반환값 : [1, 6, 7]


'''
Note:
- sort() 내부는 Insertion sort와 Merge sort를 결합한 Tim sort를 쓴다. 시간복잡도는 O(NlogN)
    - https://d2.naver.com/helloworld/0315536
- 입력크기가 10⁵일 때, O(NlogN)은 10⁵ X 16.61 이기 떄문에 O(NlogN)의 복잡도를 가지는 것은 괜찮다. O(N²)이 되는 정렬로 풀면 시간초과 나서 통과 못함
- sort() or sorted()
- 최종 시간복잡도는 O(NlogN)
''' 