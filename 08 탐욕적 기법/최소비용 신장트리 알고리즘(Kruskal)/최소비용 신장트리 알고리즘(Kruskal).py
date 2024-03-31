# 서로소 집합 클래스
class disjointSets:
    def __init__(self, n):
        self.parent = [-1]*n    	# 각 노드는 모두 루트 노드
        self.set_size = n       	# 전체 집합의 개수	

    def find(self, id) :			# 정점 id가 속한 집합의 대표번호 탐색
        while (self.parent[id] >= 0) :	# 부모가 있으면(-1이 아닌 동안)
            id = self.parent[id]	# id를 부모 id로 갱신
        return id				# 최종 id 반환. 루트 노드의 id임

    def union(self, s1, s2) :		# 두 집합을 병합(s1을 s2에 병합시킴)
        self.parent[s1] = s2		# s1을 s2에 병합시킴
        self.set_size = self.set_size-1	# 집합의 개수가 줄어 듦


# 1번을 해보세요!
def MSTKruskal(V, adj):  # 정점리스트, 간선배열 
    n = len(V)  # 정점의 개수
    dsets = disjointSets(n)  # 객체 생성 및 초기화 
    E= []  # 간선리스트 
    for i in range(n-1):  # 모든 간선을 리스트에 넣음 
        for j in range(i+1,n):
            if adj[i][j] != None:
                E.append((i, j, adj[i][j]))  # 튜플로 저장
    
    E.sort(key=lambda e: e[2])  # 가중치를 중심으로 오름차순 정렬
    
    ecount = 0  # 간선

    for i in range(len(E)):
        e= E[i]
        uset = dsets.find(e[0])  # 두 정점이 속한 집합의 루트
        vset = dsets.find(e[1])

        if uset != vset:  # 두 루트가 다르면 
            dsets.union(uset, vset)  # 두 집합을 합함
            print("간선 추가 : (%s, %s, %d)" % (V[e[0]], V[e[1]], e[2]))
            ecount += 1  # 간선이 추가됨 
            if ecount == n-1:  # 모든 간선 선택
                break


# 2번을 해보세요!
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
print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)