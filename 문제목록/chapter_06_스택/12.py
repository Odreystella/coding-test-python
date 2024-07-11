'''
문제 12

난이도: ⭐️⭐️
저자 권장 시간: 40분
권장 시간 복잡도: O(N)
출제: 프로그래머스
정답률: 57%
날짜: 2024-06-25 화요일

제약조건:
    - prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
    - prices의 길이는 2 이상 100,000 이하입니다.

입출력의 예:
    - prices	        return
    - [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''


# 시간 복잡도 O(N^2)
def solution1(prices):
    answer = []
    for i in range(len(prices)):  # O(N)
        count = 0
        for j in range(i, len(prices)-1):  # O(N)
            count += 1
            if prices[i] > prices[j+1]:  # 이전 주식 가격보다 떨어졌는지 비교
                answer.append(count)  # O(1)
                break
        else:  # 이전 주식가격보다 떨어지지 않은 경우
            answer.append(count)  # for ~ else 구문: for문이 break에 의해 끝나지 않고 끝까지 수행된 경우 동작하는 구문
    return answer


# range 부분 이렇게 하는게 더 좋은 표현인듯.
def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1 
            if prices[i] > prices[j]: # 이전 가격이 더 클 때 = 주식 가격이 떨어짐
                answer.append(count)
                break
        else:
            answer.append(count)
    return answer


# 저자 풀이
# 시간 복잡도 O(N)
def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return


# TEST 코드 입니다. 실행시켜보세요
print(solution([1, 2, 3, 2, 3])) # 반환값 : [4, 3, 1, 1, 0]
print(solution([1, 6, 9, 5])) # 반환값 : [3,2,1,0]


"""
Note:
- 미니 프로젝트 진행하느라 너무 오랜만에 문제를 풀었다..! 무려 12일만이라니 반성하자..
- 문제 읽고 고민한 내용
    - prices의 길이는 10^5이라, O(N^2)으로 풀면 시간초과 가능성 있음. 그 아래로 풀어야 함.
    - 2중 for으로 배열을 순회하면서 현재 인덱스부터 다음 배열까지 비교해서 풀면 O(N^2)이 된다.
    - 스택 챕터에 있기 때문에 스택을 사용하는 방법을 생각해보면,, 
        - 배열을 순회하며 현재 있는 값을 stack에 푸쉬하고, 해당 값보다 작은 값이 나올 때 pop하면 되지 않을까?
            - 결과적으론 nope..
        - 근데 몇초간 떨어지지 않은건 어떻게 구하지..
    - 잘 생각이 안나서 일단 2중 for문으로 풀었다ㅜㅜ 확실히 프로그래머스 돌리면 통과는 하는데 오래걸림..
    - 그래도 10.py에서 익혔던 for ~ else 구문을 사용해보았다.
    - O(N^2) 코드 프로그래머스 기준 효율성테스트에서 테스트1(140.37ms), 테스트3(175.58ms), 테스트5(86.28ms) 정도 걸린다.
    - O(N)으로 풀면 테스트1(23.91ms), 테스트3(26.61ms), 테스트5(14.58ms) 걸린다. 차이 많이 난다,,
- 저자의 풀이와 비교해봤을 때 배울 점
    - 생각해보지 못한 아이디어라서 시간을 두고 이해가 필요할것 같다.
    - 스택을 활용해서 스택에는 이전 주식의 인덱스를 담고 현재 주식과 비교하는 역할로 쓰인다.
    - 스택에는 이전 주식이 더 클때 pop되고 남은 원소들은 주식가격이 떨어지지 않은 애들이다.
"""
