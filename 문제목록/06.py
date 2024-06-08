'''
문제 06 실패율

난이도: ⭐️⭐️
저자 권장 시간: 60분
권장 시간 복잡도: O(M + NlogN)
출제: 2019 KAKAO BLIND RECRUITMENT
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


# 시간 복잡도 O(M) * O(N) ≈ O(N^2)
def solution(N, stages):
    players_by_stages = {}  # 처음에 생각 못했던 부분
    total_players = len(stages)
    total_stages = [i for i in range(1, N + 1)]

    for stage in total_stages:  # O(M)
        cur_stage_player = stages.count(stage)  # O(N)
        if cur_stage_player == 0:  # 처음에 생각 못했던 부분
            players_by_stages[stage] = 0
        else:
            players_by_stages[stage] = cur_stage_player / total_players
            total_players -= cur_stage_player

    result = sorted(players_by_stages, key=lambda k: players_by_stages[k], reverse=True) # 딕셔너리의 value를 기준으로 정렬하는 방법
    return result



# 저자 풀이
# 시간 복잡도 O(M + NlogN)
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


"""
Note:
- stages 길이를 봤을 때 10^5정도라 O(N^2) 으로 풀면 효율성 테스트에서 통과되지 못할 수 있다.
    - 내가 푼 코드는 효율성이 O(N^2)이라 좋지 못한 코드다.
    - 라인 36에서 stages.count(stage) 부분이 O(N)이 걸리는데, 이 부분을 다른 방법으로 생각해봐야 한다.
    - 나는 N으로 스테이지를 초기화해서 반복문을 돌면서 계속 그 스테이지에 있는 플레이어들을 count()로 구하는데, 
    - 저자 풀이를 보면 처음부터 스테이지별 도전자 수를 초기화한다. 이렇게 해서 시간 복잡도가 O(N^2)되는걸 피할 수가 있다.
    - 저자 풀이를 처음 봤을 때 왜 도전자수를 초기화하는걸까? 이 부분이 꼭 필요할까? 싶었는데, 내 코드를 보니 필요한 부분이었다ㅋㅋ
    - 시간복잡도가 달라지기 때문에 프로그래머스에서 테스트 케이스에서 시간 차이가 엄청 난다.
    - 테스트 5의 경우 저자 풀이는 12.21ms 걸리는데 내 코드는 1969.33ms 걸린다 100배 이상,,
    - 테스트 22의 경우도 저자 풀이는 16.21ms 걸리는데 내 코드는 1300.96ms 걸린다 거의 100배..?엄청난 차이..
- players_by_stages를 딕셔너리로 선언해야 하는 이유는
    - 처음에는 리스트로 선언하고, 실패율을 append를 해서 인덱스를 구해서 스테이지를 구해야지 했는데(프로그래머스 진료순서 정하기 문제처럼)
    - .index()는 같은 값이 있을 떄, 첫번째 찾은 원소의 인덱스만 구할 수 있어서 스테이지를 리턴했을 때 [3, 4, 1, 1, 5] 이렇게 나왔다.
    - 실패율이 [0.0, 0.0, 0.0, 1.0] 이렇게 나오고 0.0의 인덱스를 구하면 0번째 원소의 스테이지밖에 구할수가 없다.
    - 그래서 스테이지 별 실패율을 저장할 수 있게 딕셔너리가 필요하다.
- 딕셔너리의 value를 기준으로 정렬하는 방법 참고
    - https://velog.io/@isabel_noh/Python-Dictionary-Key-Value%EB%A1%9C-%EB%82%B4%EB%A6%BC%EC%B0%A8%EC%88%9C%EC%98%A4%EB%A6%84%EC%B0%A8%EC%88%9C-%ED%95%98%EA%B8%B0
- 그래도!! 다는 아니더라도 오래 걸렸지만 일단 내가 생각한 방식으로 풀었다는 거에 큰 의의를... 👏🏻👏🏻👏🏻 3개월 뒤에는 반드시 성장해 있을것이다.
"""
