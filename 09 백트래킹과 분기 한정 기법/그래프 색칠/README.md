### 그래프 색칠 | p.390
그래프에서 인접한 노드가 같은 색을 갖지 않도록 k개의 색을 이용해 칠하는 문제를 생각해 봅시다. 백트래킹을 통해 이 문제를 효율적으로 해결해 봅시다.

백트래킹은 첫 번째 정점부터 시작하여 순서에 따라 한 정점씩 색칠하는 방법을 사용합니다.
정점 v에 어떤 색 c를 칠하기 위해 먼저 v의 인접 정점을 조사합니다. v의 인접 정점 중 색이 c인 정점이 있으면 백트래킹하고 다른 색을 시도합니다. 만약 v에 c를 칠했다면 다음 노드를 같은 방법을 처리합니다. 이 과정을 그래프의 모든 노드가 색칠될 때까지 반복합니다. 모든 노드를 검사했는데도 해가 없으면 이 트리는 k개의 색으로는 칠할 수 없는 것입니다.

---

1. 그래프 g의 정점 v에 색상 c를 칠할 수 있는지 유효성을 검사하는 함수 isSafe(g, v, c, color)를 완성해 보세요.

* g는 그래프를 나타내며, 인접 행렬로 주어져요.
* v는 그래프의 v번째 정점임을 의미해요.
* c는 색상을 의미해요.
* color는 지금까지 칠해진 색상 표예요.
* 모든 인접 정점을 검사해 하나라도 이미 색상 c가 칠해져 있는 정점이 있다면 v에는 c를 칠할 수 없어요. 따라서 False를 반환해요.

2. 백트래킹을 이용한 상태 공간 트리 탐색 함수인 DFS_graph_coloring(graph, k, v, color)을 완성해 보세요.

* 인접 행렬로 주어지는 그래프 graph, 색상 수 k, 현재 정점 인덱스 v, 정점별 색상을 저장한 리스트 color가 입력돼요.
* 정점의 인덱스 v가 정점의 수와 같으면 이미 모든 정점을 칠한 경우이므로 그래프 색칠에 성공했기 때문에 True를 반환해요.
* v에 모든 색상 c를 적용해보고, isSafe(g, v, c, color) 함수를 호출하여 c가 칠할 수 있는 색상임이 검증되면 일단 칠하고, 나머지 정점들을 순환적으로 검사해요. 이제 v+1번째 정점을 검사해야 하는데, 이것이 가능하다면 답이 나온 것이고, 아니면 다른 색을 시도해요.
* 모든 색상에 대해 성공하지 못했으면 그래프 색칠에 실패한 것이므로 False를 반환해요.

3. 사용할 색상 수 k를 입력받아 보세요.