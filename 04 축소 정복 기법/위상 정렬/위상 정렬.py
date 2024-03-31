# 1번을 해보세요!
def topological_sort(graph):
    inDeg = {} # 각 정점의 진입차수 저장 
    for v in graph:
        inDeg[v] = 0  # 각 정점의 진입차수 초기화
    for v in graph:
        for u in graph[v]:
            inDeg[u] += 1  # 모든 정점으로 '들어가는' 간선 수를 구해 진입차수 구함

    # 진입차수가 0인 정점을 찾아서 vlist에 삽입
    # 진입차수가 0이어야 선행 순서를 지킬 수 있기 때문 
    vlist = []
    for v in graph:
        if inDeg[v]==0:
            vlist.append(v)
    
    # vlist에서 하나를 추출하여 순회하며 연결된 정점의 진입차수를 1씩 차감 -> vlist가 빌 때까지 반복
    while vlist:
        v = vlist.pop()  # 우선 하나씩 추출하며 출력해주고
        print(v, end=' ')
        
        for u in graph[v]:
            inDeg[u] -= 1  # 추출된 v와 연결되어 있으면 1씩 차감
            if inDeg[u] == 0:
                vlist.append(u)  # 진입차수가 0이 되면 vlist에 삽입 
    return None


# 2번을 해보세요!
# 딕셔너리에서 key값인 알파벳을 (정점의 개수만큼)지정하고 value인 공집합 생성 
mygraph = dict()
for i in range(int(input())):
    mygraph[chr(ord('A')+i)] = set()  

# 간선의 개수에 맞는 graph 생성
for _ in range(int(input())):
    e1, e2 = input().split()[:2]
    mygraph[e1].add(e2)

# 출력합니다!
print('topological_sort: ')
topological_sort(mygraph)
print()