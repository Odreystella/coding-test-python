"""
문제 56

난이도: ⭐️ 
저자 권장 시간: 30분
권장 시간 복잡도: O(NlogN)
출제: 프로그래머스
정답률: 69%
날짜: 2024-08-18 일요일

제약조건:
    - strings는 길이 1 이상, 50이하인 배열입니다.
    - strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
    - strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
    - 모든 strings의 원소의 길이는 n보다 큽니다.
    - 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

입출력의 예:
    - strings	               n	return
    - ["sun", "bed", "car"]	   1	["car", "bed", "sun"]
    - ["abce", "abcd", "cdx"]  2	["abcd", "abce", "cdx"]
"""


# 시간 복잡도 
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print(solution(["sun", "bed", "car"], 1)) # 반환값 : ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2)) # 반환값 : ["abcd", "abce", "cdx"]


"""
Note:
- 문제 읽고 고민한 내용
    - sorted()와 key 함수를 쓰면 간단한 문제!
- 저자의 풀이와 비교해봤을 때 배울 점
    - 풀이가 다를게 없다!
"""
