"""
문제 39 너비 우선 탐색 순회

난이도: ⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(N+E)
출제: 저자 출제
날짜: 2024-08-01 목요일

제약조건:
    - 노드의 최대 개수는 100개입니다.
    - 시작 노드부터 시작해서 노드를 방문할 수 있는 경로가 항상 있습니다.
    - 그래프의 노드는 숫자입니다.

입출력의 예:
    - graph [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]
    - start 1
    - return [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


# 시간 복잡도 
def solution():
    return


# 저자 풀이
# 시간 복잡도 O(N+E) N: 노드의 갯수, E: 간선의 갯수
from collections import defaultdict, deque


def bfs(adj_list, start):
    visited = set()  # 방문 표시

    queue = deque([start])  # deque()는 이터러블 객체를 인수로 받음
    visited.add(start)

    # result = []
    # result.append(start)

    while queue:
        node = queue.popleft()  # 큐에 있는 원소중에 가장 먼저 푸시된 원소를 팝한 값
        for neighbor in adj_list.get(node, []):  # 팝한 노드의 인접한 이웃 노드들 가져오기
            if neighbor not in visited:  # 인접한 노드가 방문되지 않은 경우
                queue.append(neighbor)  # 큐에 푸시하고
                visited.add(neighbor)  # 방문 처리
                # result.append(neighbor)

    return list(visited)


def solution(graph, start):
    adj_list = defaultdict(list)  # 그래프를 인접 리스트로 변환

    for u, v in graph:
        adj_list[u].append(v)

    result = bfs(adj_list, start)

    return result


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
graph = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]
start = 1
print(solution(graph, start)) # 반환값 : [1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
Note:
- 문제 읽고 고민한 내용
- 저자의 풀이와 비교해봤을 때 배울 점
    - bfs 개념을 코드로 짜면 이런거구나 코드 보면서 이해하려고 했음.
"""
