'''
문제 08 괄호 짝 맞추기

난이도: ⭐️⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(N)
출제: 저자 출제
날짜: 2024-06-08 토요일

제약조건:
    - 열린 괄호는 자신과 가장 가까운 닫힌 괄호를 만나면 상쇄됩니다.
    - 상쇄 조건은 열린 괄호가 먼저 와야 하고, 열린 괄호와 닫힌 괄호 사이에 아무것도 없어야 합니다.
    - 더 상쇄할 괄호가 없을 때까지 상쇄를 반복합니다.

입출력의 예:
    - s        반환값
    - (())()   True
    - ((())()  False
    - ))(())   False
'''


# 시간 복잡도 O(N)
def solution(s):
    stack = []
    for item in s:
        if len(stack) == 0 and item == ')':
            return False

        if item == '(':
            stack.append(item)  # 시간복잡도 O(1)
        else:
            stack.pop()  # 시간복잡도 O(1)

    return len(stack) == 0


# 저자 풀이
# 시간 복잡도 O(N)
def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution("(())()")) # 반환값 : True
print(solution("((())()")) # 반환값 : False
print(solution("))(())")) # 반환값 : False


"""
Note:
- "(" 일 때, 스택에 push한다. 스택이 가득 찼는지 안찾는지는 확인할 필요 없음
- ")"일 떄 스택이 비어있는지 확인하고, 있으면 pop한다. 
    - 스택이 비어있는데 pop하면 에러나기 때문에 False. 
- 끝까지 갔을 때 그 떄 스택에 남은게 있으면 괄호 짝이 안맞는거
"""
