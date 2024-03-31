INF = 9999

# dist 배열에서 최소 가중치를 가진 정점을 찾는 알고리즘 
def getMinVertex(dist, selected) :
    minv = -1	# 정점 선택 
    mindist = INF  # 거리 
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:  # v가 선택되지 않았고, 최소 거리가 가장 짧을 때 
            mindist = dist[v]
            minv = v
    return minv

# Prim의 MST(최소비용 신장 트리) 알고리즘
def MSTPrim(vertex, adj) :  # 정점리스트, 인접행렬
    vsize = len(vertex)
    dist = [INF] * vsize
    dist[0] = 0  # dist: [0. inf, inf ...]
    selected = [False] * vsize  # selected: 선택된 정점 리스트

    for i in range(vsize):  # 정점 수만큼 반복 
        u = getMinVertex(dist, selected)  # 거리가 가장 가까운 정점 
        selected[u] = True
        print(vertex[u], end=':')  # 선택된 u 출력 
        print(dist)  # 현재까지 선택된 정점과 다른 정점들 사이의 최소거리 

        for v in range(vsize):  # 임의의 v
            if(adj[u][v] != None):  # u와 v가 인접하고 
                if selected[v]==False and adj[u][v] < dist[v]:  # v가 선택되지 않은 정점이자 인접 거리가 더 작을 때
                    dist[v] = adj[u][v]  # 최소거리 갱신 


# 3번을 해보세요!
vertex = [n for n in input().split()]
n = int(input())
weight = [[None] * n for _ in range(n)]
for _ in range(n):
    edge = input().split()
    node1 = edge[0]
    node2 = edge[1]
    w = int(edge[2])

    i = vertex.index(node1)
    j = vertex.index(node2)

    weight[i][j] = w
    weight[j][i] = w

# 출력합니다!
print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)