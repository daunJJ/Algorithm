### 분기 한정 기법을 이용한 0-1 배낭 채우기 | p.399
0-1 배낭 채우기 문제는 무게와 가치가 주어진 n개의 물건이 있을 때, 배낭에 담을 수 있는 최대 무게(용량) W를 초과하지 않으면서 물건들의 가치의 합이 최대가 되도록 만들어야 하는 문제입니다.

어떤 노드의 무게 합이 이미 배낭 용량을 초과했다면 서브 트리를 더 탐색할 필요가 없다는 아이디어를 이용하여 백트래킹 전략으로 이 문제를 해결할 수 있습니다.

이때, 분기 한정(branch and bound)을 이용하면 백트래킹의 효율을 추가로 향상할 수 있습니다. 분기 한정은 N의 서브 트리에서 기대할 수 있는 최대 가치를 먼저 계산합니다.

만약 최대 기대 가치가 10이라고 하면, N의 서브 트리에서는 N까지 확정된 가치 60과 최대 기대 가치 10을 합한 70 이상의 해가 나올 수 없습니다. 현재 알고 있는 최대 가치가 80이라고 할 때 이 서브 트리를 탐색할 필요가 없으므로 바로 백트래킹 합니다.

분기 한정을 위해서는 상태 공간 트리의 각 노드를 탐색할 때마다 지금까지 알고 있는 최적해인 최고가치(maximum profit) 과 현재 노드 N에서 기대할 수 있는 최선의 가치합인 한계 가치(bounded profit) 을 계산해야 함에 유의하며 분기 한정 기법을 이용해 0-1 배낭 채우기 문제를 해결해 봅시다.

---

1. 분기 한정을 이용한 0-1 배낭 채우기 함수 knapSack_bnb(obj, knapsack, W, level, weight, profit, maxProfit, bound)를 완성해 보세요.

* obj는 물건들의 리스트, W는 배낭의 용량, level은 현재 노드의 레벨로, 루트 노드의 레벨은 0으로 생각해요.
* profit은 각각 루트에서 현재 노드까지 경로상의 물건과 가치 합을 나타내고, maxProfit은 지금까지의 최고 합(최고가치)를 나타내요.
* 함수 knapSack_bnb의 가장 첫 번째 줄은 출력 함수printNode(knapsack, level, weight, profit, bound, maxProfit)로 고정되어 있어요.
* 단말 노드까지 처리되었으면 지금까지의 최고 합을 반환해요.
* level 번째 항목을 넣는 경우, 추가한 항목에 의해 배낭 용량이 넘치지 않아야 계속 탐색을 진행해요.
* 배낭의 무게 합과 가치 합을 갱신해요. 만약 현재의 확정된 가치 합이 최고 합보다 크면 최고 합을 갱신해요.
* bound1 함수를 이용해서 한계 합을 계산하고, 이 값이 최고 합보다 큰 경우에만 서브 트리를 탐색해요. 순환 호출에서 level은 증가하여야 하고, 현재의 무게 합과 가치 합을 전달해야 함에 유의해요.
* level 번째 항목을 넣지 않는 경우, 무게 합과 가치 합은 변화 없고, 한계 합을 계산하여 최고 합보다 큰 경우에만 서브 트리를 계속 탐색하고, 그렇지 않으면 백트래킹 해요.

2. 어떤 노드 N의 한계 가치를 구하는 함수 bound1(obj, W, level, weight, profit)를 완성해 보세요.

* obj는 물건들의 리스트, W는 배낭의 용량, level은 현재 노드의 레벨로, 루트 노드의 레벨은 0으로 생각해요.
* weight와 profit는 각각 루트에서 현재 노드까지 경로상의 물건의 무게 합과 가치 합이에요.
* 무게 합이 용량을 초과하면 불가능한 해이므로 백트래킹 하는데, 이때 한계 합을 0으로 반환해요.
* 한계 합은 현재 노드까지 확정된 합 profit에 남은 모든 물건을 넣었을 때 얻을 수 있는 가치들의 합으로 계산해요. 이를 반환해요.

3. 물건들의 리스트 obj와 배낭의 용량 W를 입력받아 보세요.

* 첫 번째 줄에는 obj에 들어갈 물건의 개수가 주어져요.
* 두 번째 줄부터 첫 번째 줄에 주어진 물건의 개수 개의 줄 만큼 무게, 가치, 물건이 공백으로 구분되어 주어져요. 무게와 가치는 양의 실수로, 물건은 문자열로 주어져요. 이를 튜플 형태로 받아 obj에 저장해 보세요.
* 마지막 줄에는 배낭의 용량 W에 들어갈 값을 줘요.
* 예를 들어, 위 입력 예시는 아래와 같이 저장돼요.