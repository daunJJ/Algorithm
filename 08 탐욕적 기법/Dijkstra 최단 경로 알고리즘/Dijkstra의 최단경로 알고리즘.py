# 다익스트라 최단경로 알고리즘 
def shortest_path_dijkstra(vtx, adj, start) :  # 정점 리스트, 간선 가중치 배열, 시작 정점
    vsize = len(vtx)  # 정점 수
    dist = list(adj[start])  # dist 배열 생성 및 초기화 
    dist[start] = 0  # 시작 정점의 거리 = 0
    path = [start] * vsize  # path 배열 생성 및 초기화: 경로 자체를 구하기 위함 
    found = [False] * vsize  # found 배열 생성 및 초기화
    found[start] = True  # 시작정점: 이미 찾아짐 

    for i in range(vsize):
        print("Step%2d: " % (i + 1), dist)
        u = getMinVertex(dist, found)  # dist 리스트에서 거리가 최소인 정점을 찾음 
        found[u] = True

        for w in range(vsize):
            if not found[w]:
                if dist[u] + adj[u][w] < dist[w]:  # 거쳐가는게 더 짧으면 
                    dist[w] = dist[u] + adj[u][w]  # 거리 갱신 
                    path[w] = u  # 경로 저장 
    return path


# dist 배열에서 최소 가중치를 가진 정점을 찾는 함수
def getMinVertex(dist, selected) :
    minv = -1
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv


# 2번을 해보세요!
INF = 9999
vertex = input().split()
num_vertex = len(vertex)
weight = [[INF] * num_vertex for _ in range(num_vertex)]

n = int(input())

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
print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)):
    if end != start:
        print("[최단경로: %s->%s] %s" %
              (vertex[start], vertex[end], vertex[end]), end='')
        while path[end] != start:
            print(" <- %s" % vertex[path[end]], end='')
            end = path[end]
        print(" <- %s" % vertex[path[end]])
