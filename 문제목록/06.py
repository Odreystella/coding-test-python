'''
문제 06 실패율

난이도: ⭐️⭐️
저자 권장 시간: 60분
권장 시간 복잡도: 
출제: 프로그래머스
정답률: 60%
날짜: 2024-06-03 월요일, 2024-06-05 수요일

제약조건:
    - 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
    - stages의 길이는 1 이상 200,000 이하이다.
    - stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
        - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
        - 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
    - 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
    - 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

입출력의 예:
    - N	stages	                 result
    - 5	[2, 1, 2, 6, 2, 4, 3, 3] [3, 4, 2, 1, 5]
    - 4	[4, 4, 4, 4, 4]	         [4, 1, 2, 3]
'''


def solution(N, stages):
    answer = {}
    total_players = len(stages)

    total_stages = [i for i in range(1, N+1)]
    for stage in total_stages:
        if total_players == 0:
            answer[stage] = 0
        else:
            cur_stage_player = stages.count(stage)
            fail = cur_stage_player / total_players
            answer[stage] = fail
            total_players -= cur_stage_player

    result = sorted(answer, key=lambda k:answer[k], reverse=True) 
    return result


# 다른 사람 풀이
def solution(N, stages):
    challenger = [0] * (N + 2)
    for stage in stages:
        challenger[stage] += 1

    fails = {}
    total = len(stages)

    for i in range(1, N + 1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]

    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    return result


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # 반환값 : [3, 4, 2, 1, 5]
# print(solution(4, [4, 4, 4, 4, 4])) # 반환값 : [4, 1, 2, 3]


'''
Note:
- 최종 시간복잡도는 O(M+NlogN)
''' 
