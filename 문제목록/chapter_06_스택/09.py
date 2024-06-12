'''
문제 09 10진수를 2진수로 변환하기

난이도: ⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(logN)
출제: 저자 출제
날짜: 2024-06-11 화요일

제약조건:
    - 없음

입출력의 예:
    - decimal    반환값
    - 10         1010
    - 27         11011
    - 12345      11000000111001
'''


# 시간 복잡도 O((logN)^2)
def solution(decimal):
    stack = []
    while decimal >= 1: # O(logN)
        res = decimal % 2
        stack.append(res) # O(1)
        decimal = int(decimal / 2)

    result = ""
    while len(stack) > 0: # O(stack의 크기만큼) = O(logN)
        top = stack.pop() # O(1)
        result += str(top) # += 연산자는 수행할 때마다 객체를 새로 생성하므로 O(logN)
    return result


# 시간 복잡도 O(logN)의 풀이
# 저자 풀이에서 stack.pop()을 쓰지 않고, join()메서드를 쓰면 O(logN)이 된다고 하여 수정해보았다.
def solution(decimal):
    stack = []
    while decimal >= 1: # O(logN)
        res = decimal % 2
        stack.append(str(res)) # O(1)
        decimal = int(decimal / 2)

    # return "".join(list(reversed(stack))) # stack[::-1]보다 메모리 효율이 더 좋다고 한다.
    return "".join(stack[::-1]) # stack[::-1]하면 stack을 뒤집어 준다


# 저자 풀이
# 시간 복잡도 O((logN)^2)
def solution(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2

    binary = ""
    while stack:
        binary += stack.pop()

    return binary

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(10)) # 반환값 : 1010 
# print(solution(27)) # 반환값 : 11011
# print(solution(12345)) # 반환값 : 11000000111001


"""
Note:
- 문제 읽고 고민한 내용
    - 스택에 있는 문제인데 이 문제를 왜 스택으로 풀어야 하는 걸까 고민이 되었다.
    - 일단 10, 27을 2진수로 표현하기 위해 나눠봤는데, 결과적으로 각 단계별 2로 나눈 나머지 값을 거꾸로 읽어야 했다.
    - 그래서 처음 2로 나눈 나머지 값을 스택에 담고, 나눌 수 있는 만큼 나눈 다음에 스택에서 pop한 값들을 이어붙이면 되겠다 라는 생각이 들었다.
- 저자의 풀이와 비교해봤을 때 배울 점
    - 2로 나눈 나머지 값을 뭐라고 네이밍할 지 고민하다가 생각이 안나서 res로 했는데, remainder라는 네이밍이 더 좋은것 같다.
    - 한번 나누고 decimal 값을 변경해줘야 하는데 // 몫 연산자가 생각이 안나서, int(decimal / 2)를 할당해버렸는데 좋지 않은것 같다ㅎㅎ
    - while 조건문도 decimal >= 1 보다 decimal > 0이 더 좋은것 같다.
    - += 연산자는 수행할 때마다 객체를 새로 생성하는지 몰랐다.
- 저자의 풀이에서 시간복잡도를 O((logN)^2)를 O(logN)을 줄이기 위해 리스트의 join()를 활용하면 된다고 해서 수정해보았다.
    - 이렇게 풀기 위해서는 stack를 거꾸로 뒤집어야 했는데, 그때 슬라이싱으로 뒤집거나 리스트의 메서드 reversed(), reverse()를 써보았다.
    - 처음엔 pop()할 때 str으로 변환했었는데, append()할 때 str로 넣어야 join()메서드 쓸 때 연산이 가능하다.
    - 차이점이 잘 정리되어 있다. https://www.daleseo.com/python-reversed/
"""
