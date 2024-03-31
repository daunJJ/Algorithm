# 1번을 해보세요!
def dfs(graph, start, visited ):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited  # graph는 딕셔너리, 딕셔너리의 value는 set
                                      # graph[start] = start노드의 인접 노드 
                                      # graph[start] - visited = 방문하지 않은 인접노드
        for v in nbr:  # 인접노드에 대해 다시 탐색
            dfs(graph, v, visited)

# 2번을 해보세요!
mygraph = dict()
n = int(input())  # 간선의 개수부터 받음
for i in range (n):
    e1, e2 = input().split()[:2]  # 인접한 노드 쌍을 받음
    mygraph[e1] = mygraph.setdefault(e1, set()) | {e2}  # 없으면 공집합 생성, 그 집합에 e2를 더해줌 
                                                        # 있으면 원래 집합 반환, 그 집합에 e2 더해줌 
    mygraph[e2] = mygraph.setdefault(e2, set()) | {e1}  # 무향 그래프이기 때문에 따로 
 
# 출력합니다!
print('DFS : ', end='')
dfs(mygraph, "A", set() )
print("# 무방향 그래프이기 때문에 출력 값이 매번 바뀌어요.")