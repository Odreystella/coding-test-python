"""
문제 19 문자열 해싱을 이용한 검색 함수 만들기

난이도: ⭐️⭐️
저자 권장 시간: 40분
권장 시간 복잡도: O(N+K)
출제: 저자 출제
날짜: 2024-07-14 일요일

제약조건:
    - 입력 문자열은 영어 소문자로만 이루어져 있습니다.
    - 문자열의 최대 길이는 10^6입니다.
    - 해시 충돌은 없습니다.
    - 아래와 같은 문자열 해싱 방법을 활용해서 해싱 함수를 구현하세요.
    - 다음 식에서 p는 31, m은 1,000,000,007로 합니다.
        - hash(s) = (s[0] + s[1]*p + s[2]*p^2 ...... s[n-1]*p^n-1) mod m

입출력의 예:
    - string_list                     query_list                             return
    - ['apple', 'banana', 'cherry']   ['banana', 'kiwi', 'melon', 'apple']   [True, False, False, True]
"""


# 시간 복잡도
def solution1(string_list, query_list):
    dict = {}
    for q in query_list:  # O(N)
        dict[q] = False
    for s in string_list:  # O(K)
        if s in dict:
            dict[s] = True

    return [v for v in dict.values()]


# 저자 풀이
# 시간 복잡도 O(N+K)
def polynomial_hash(str):
    p = 31
    m = 1_000_000_007
    hash_value = 0
    for char in str:
        hash_value = (hash_value * p + ord(char)) % m
    return hash_value


def solution(string_list, query_list):
    hash_list = [polynomial_hash(str) for str in string_list]

    result = []
    for query in query_list:
        query_hash = polynomial_hash(query)
        if query_hash in hash_list:
            result.append(True)
        else:
            result.append(False)
    return result


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
string_list = ['apple', 'banana', 'cherry']
query_list = ['banana', 'kiwi', 'melon', 'apple']
print(solution(string_list, query_list )) # 반환값 : [True, False, False, True]


"""
Note:
- 문제 읽고 고민한 내용
    - 해싱함수를 활용해서 풀어야 하는데 그렇지 못했다..
- 저자의 풀이와 비교해봤을 때 배울 점
"""
