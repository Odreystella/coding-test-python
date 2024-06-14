'''
문제 11 짝지어 제거하기

난이도: ⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(N)
출제: 프로그래머스
정답률: 71%
날짜: 2024-06-14 금요일

제약조건:
    - 문자열의 길이 : 1,000,000이하의 자연수
    - 문자열은 모두 소문자로 이루어져 있습니다.

입출력의 예:
    - s	        result
    - baabaa    1
    - cdcd	    0
'''


# 시간 복잡도 O(N)
def solution(s):
    stack = []
    for ch in s:  # O(N)
        if stack and stack[-1] == ch:
            stack.pop()  # O(1)
        else:
            stack.append(ch)  # O(1)
    return 1 if not stack else 0


# 저자 풀이
# 시간 복잡도 O(N)
def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return int(not stack)


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution('baabaa')) # 반환값 : 1
print(solution('cdcd')) # 반환값 : 0


"""
Note:
- 문제 읽고 고민한 내용
    - 문자열의 길이가 10^6이라 O(N^2)밑으로 풀어야함
    - 반복문 돌면서 일단 stack에 순회중인 문자열 append하고, stack의 top과 비교해서 현재 문자열과 같으면 pop하기
- 저자의 풀이와 비교해봤을 때 배울 점
    - 접근 방식은 같았다! yeah
    - 결과 리턴할 때, 한줄 조건문 썼는데 int(not stack) 깔끔하다
"""
