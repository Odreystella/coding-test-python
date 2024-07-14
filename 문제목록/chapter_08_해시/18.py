"""
문제 18 두 개의 수로 특정값 만들기

난이도: ⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(N+K)
출제: 저자 출제
날짜: 2024-07-14 일요일

제약조건:
    - n은 2 이상 10,000 이하의 자연수입니다.
    - arr의 각 원소는 1 이상 10,000 이하의 자연수입니다.
    - arr의 원소 중 중복되는 원소는 없습니다.
    - target은 1 이상 20,000 이하의 자연수입니다.

입출력의 예:
    - arr	            target   return
    - [1, 2, 3, 4, 8]	6         True
    - [2, 3, 5, 9]      10        False
"""


# 시간 복잡도 O(N^2)
def solution(arr, target):
    dict = {}
    for num1 in arr:  # O(N)
        num2 = target - num1
        if num1 != num2 and num2 in arr:  # O(N)
            dict[num1] = num2
    for k, v in dict.items():  # O(K)
        if k + v == target:
            return True
    return False


# 시간 복잡도 O(N^2)
def solution(arr, target):
    dict = {}
    for num1 in arr:  # O(N)
        num2 = target - num1
        if num1 != num2 and num2 in arr:  # O(N)
            dict[num1] = num2

    return bool(dict)


# 저자 풀이
# 시간 복잡도 O(N+K)
def count_sort(arr, k):
    hashtable = [0] * (k + 1)

    for num in arr:
        if num <= k:
            hashtable[num] = 1

    return hashtable


def solution(arr, target):
    hashtable = count_sort(arr, target)  # O(K)

    for num in arr:  # O(N)
        num2 = target - num

        if (num2 != num and num2 >= 0 and num2 <= target and hashtable[num2] == 1):
            return True
    return False


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution([1, 2, 3, 4, 8], 6)) # 반환값 : True
print(solution([2, 3, 5, 9], 10)) # 반환값 : False


"""
Note:
- 문제 읽고 고민한 내용
    - 먼저 이중 for문으로 두 수를 골라 더하는 방법이 먼저 생각났다.
    - 문제가 해시 파트에 있어서 어떻게 해시로 풀 수 있을지 고민해보았는데..
    - for 문을 돌면서 현재 순회중인 수를 target에서 뺐을 때, 나온 결과값이 arr에 있는 경우에만 딕셔너리에 저장했다.
    - in을 쓰면 시간 복잡도가 O(N)이라 조건문이 True인 경우에는 O(N^2)의 시간복잡도가 나온다,,흠

- 저자의 풀이와 비교해봤을 때 배울 점
    - 해시라고 해서 딕셔너리를 쓰는건줄 알았는데 그건 아니었다.
    - 문제를 쪼개서 다른 함수로 만드는 것도 좋다고 생각했다.
    - count_sort()에서 target의 크기만큼 배열을 0으로 초기화한 후, arr에 있는 값들 중 target보다 작은 수만 1로 변경했다.
    - solution()에서 target - num 한 값이 num과 다르고, 0 이상 target보다 작아야 하며, hashtable에 있는 수 일 때 True를 반환하는 로직이다.
    - 두 수를 골라서 더할 때, 무작정 모든 경우의 수를 다 구해서 더해보는게 아니라 이런 방식으로 구할 수 있다는걸 배웠다.
"""
