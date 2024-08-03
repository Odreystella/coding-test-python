"""
문제 38 깊이 우선 탐색 순회

난이도: ⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(N+E)
출제: 저자 출제
날짜: 2024-08-02 금요일

제약조건:
    - 노드의 최대 개수는 100개를 넘지 않습니다.
    - 시작 노드부터 시작해서 모든 노드를 방문할 수 있는 경로가 항상 있습니다.
    - 그래프의 노드는 문자열입니다.

입출력의 예:
    - graph [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
    - start 'A'
    - return ['A', 'B', 'C', 'D', 'E']

    - graph [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
    - start 'A'
    - return ['A', 'B', 'D', 'E', 'F', 'C']
"""


from collections import defaultdict


def dfs_stack(adj_list, node, visited=[]):
    """
    DFS를 스택으로 구현하는 방법
    """
    stack = [node]

    while stack:
        recent_node = stack.pop()
        visited.append(recent_node)

        for neighbor in adj_list.get(recent_node, [])[::-1]:
            if neighbor not in visited:
                stack.append(neighbor)

    return visited


def solution(graph, start):
    adj_list = defaultdict(list)

    for u, v in graph:
        adj_list[u].append(v)

    result = dfs_stack(adj_list, start, visited=[])
    return result


graph2 = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
print(solution(graph2, 'A')) # 반환값 : ['A', 'B', 'D', 'E', 'F', 'C']


def dfs_recursive(adj_list, node, visited):
    """
    DFS를 재귀로 구현하는 방법
    """
    visited.append(node)

    for neighbor in adj_list.get(node, []):
        if neighbor not in visited:
            dfs_recursive(adj_list, neighbor, visited)

    return visited


def solution(graph, start):
    adj_list = defaultdict(list)

    for u, v in graph:
        adj_list[u].append(v)

    result = dfs_recursive(adj_list, start, visited=[])
    return result


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# graph1 = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
# print(solution(graph1, 'A')) # 반환값 : ['A', 'B', 'C', 'D', 'E']

graph2 = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']]
print(solution(graph2, 'A')) # 반환값 : ['A', 'B', 'D', 'E', 'F', 'C']



"""
Note:
- DFS는 스택과, 재귀 2가지 방법으로 풀 수 있어서 두개의 템플릿 코드를 공부함
- 1. 스택
    - 스택에 시작 노드 푸시
    - 스택 pop
    - 팝한 노드 방문 처리
    - 팝한 노드 인접 노드 중에서 미방문 노드 푸시
    - 스택이 빌 때까지 반복
- 2. 재귀
    - 시작 노드 방문 처리
    - 시작 노드의 인접 노드 중에서 미방문 노드일 때
        - 재귀 호출
"""
