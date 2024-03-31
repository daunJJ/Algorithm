# 그래프 색칠 유효성 검사 
def isSafe(g, v, c, color):  # 정점 인접 배열, 정점, 색상, 색상 리스트 
    for i in range(len(g)):  # 그래프의 모든 정점 i에 대해 
        if g[v][i] == 1 and color[i] == c:  # 인접하고 색이 같으면 
            return False    
    return True

# 그래프 색칠 
def DFS_graph_coloring(graph, k, v, color):  # 정점 인접 리스트, 색상 개수, 정점 인덱스, 색상 리스트 
    if v==len(graph):  # 색칠 성공 
        return True

    for c in range(1,k+1):  # 모든 색상에 대해 
        if isSafe(graph, v, c, color):  # v를 c로 칠할 수 있으면 
            color[v] = c
            if DFS_graph_coloring(graph, k, v+1, color):
                return True
            color[v] = 0  # 복구
    return False  # 색칠 실패 

# 그래프 색칠 주 함수
def graphColouring(graph, k, states): 
    color = [0] * len(graph)       # 정점의 색 배정 리스트: 초기 0
    ret = DFS_graph_coloring(graph, k, 0, color)  # 0번 정점부터 처리
    if ret : 
        for i in range(len(graph)) :
            print("%3s = "%states[i], color_name[color[i]])
    else :
        print("그래프를 색칠할 수 없음!")


# 3번을 해보세요!
k = int(input())


# 출력합니다!
states = ['NT', 'WA', 'Q', 'SA', 'NSW', 'V']
color_name = ["none", "빨강", "초록", "파랑", "노랑", "보라"]
g = [ [0, 1, 1, 1, 0, 0],
      [1, 0, 0, 1, 0, 0],
      [1, 0, 0, 1, 1, 0],
      [1, 1, 1, 0, 1, 1],
      [0, 0, 1, 1, 0, 1],
      [0, 0, 0, 1, 1, 0],]
print("색상 %d개:" %(k))
graphColouring(g, k, states) 