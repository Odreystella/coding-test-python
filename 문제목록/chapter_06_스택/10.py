'''
문제 10 괄호 회전하기

난이도: ⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(N^2)
출제: 프로그래머스
정답률: 64%
날짜: 2024-06-12 수요일

제약조건:
    - s의 길이는 1 이상 1,000 이하입니다.

입출력의 예:
    - s	         result
    - "[](){}"	 3
    - "}]()[{"	 2
    - "[)(]"	 0
    - "}}}"	     0
'''


# 시간 복잡도 O(N^2)
def solution1(s):
    answer = 0
    rotated_s = ''

    for i in range(len(s)):  # O(N)
        stack = []
        if i == 0:
            rotated_s = s
        else:
            rotated_s = s[i:] + s[:i] # O(N)

        for j in rotated_s: # O(N)
            if len(stack) == 0 and j in '])}':
                stack.append(False)  # stack가 비어 있지 않게하려는 트릭
                break

            if j in '[({':
                stack.append(j)  # O(1)
            elif stack[-1] == '[' and j == ']':
                stack.pop()  # O(1)
            elif stack[-1] == '(' and j == ')':
                stack.pop()
            elif stack[-1] == '{' and j == '}':
                stack.pop()

        if len(stack) == 0:
            answer += 1

    return answer


# for ~ else 구문 사용
# 시간 복잡도 O(N^2)
def solution(s):
    answer = 0
    rotated_s = ''

    for i in range(len(s)):  # O(N)
        stack = []
        if i == 0:
            rotated_s = s
        else:
            rotated_s = s[i:] + s[:i] # O(N)

        for j in rotated_s: # O(N)
            if len(stack) == 0 and j in '])}':
                break

            if j in '[({':
                stack.append(j)  # O(1)
            elif stack[-1] == '[' and j == ']':
                stack.pop()  # O(1)
            elif stack[-1] == '(' and j == ')':
                stack.pop()
            elif stack[-1] == '{' and j == '}':
                stack.pop()

        else:  # 회전한 문자열이 올바른 괄호일 떄만 카운트 됨
            if len(stack) == 0:
                answer += 1

    return answer


# 저자 풀이
# 시간 복잡도 O(N^2)
def solution1(s):
    answer = 0
    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):
            c = s[(i + j) % n]
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    break

                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    break
        else:  # for ~ else 구문: for문이 break에 의해 끝나지 않고 끝까지 수행된 경우 동작하는 구문
            if not stack:
                answer += 1
    return answer


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution("[](){}")) # 반환값 : 3 
# print(solution("}]()[{")) # 반환값 : 2
# print(solution("[)(]")) # 반환값 : 0
# print(solution("}}}")) # 반환값 : 0


"""
Note:
- 문제 읽고 고민한 내용
    - s를 왼쪽으로 회전하는 건 어떻게 구현해야 하나?
        - 슬라이싱이 생각남, 시간복잡도는 O(K)
    - 회전은 range()로 s의 길이만큼 하면 될거 같은데
    - 괄호가 한짝씩 있는 거는 미리 예외처리
    - 처음에 왼쪽으로 한칸 움직이고, 그 안에서
        - 그 문자열을 돌면서 stack에 넣어보고 짝이 맞는지 체크
        - 짝이 맞으면 카운팅하는 변수값 증가
- 저자의 풀이와 비교해봤을 때 배울 점
    - c = s[(i + j) % n] 이 부분은 좀 더 이해가 필요하다.
    - for ~ else 구문! 
        - 처음에 짠 코드에서 두번째 for문에서 break에 의해 벗어났을 때도 if len(stack) == 0: 에 걸려서 
        - break하기 전에 stack가 비어있지 않게 False를 넣어주는 트릭을 썼었는데
        - for ~ else 구문을 사용하면 깔끔한 것 같다. 내가 원하는 거였다.
"""
