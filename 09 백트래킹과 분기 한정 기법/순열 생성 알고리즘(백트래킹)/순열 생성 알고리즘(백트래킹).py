# 순열 생성 알고리즘 
def all_permutations(data):
    bUsed = [False] * len(data)  # 원소의 사용 여부 
    DFS_permutation (data, [], 0, bUsed)  # 루트부터 탐색 시작 

def DFS_permutation (data, sol, level, bUsed):
    if level == len(data):  # 하나의 순열 완성 
        print(sol)
        return
    
    for i in range(len(data)):  
        if not bUsed[i]:  
            sol.append(data[i])  # 부분해에 추가 
            bUsed[i] = True  # 사용했다고 표시
            DFS_permutation(data, sol, level+1, bUsed)  # 자식 노드 탐색 
            sol.pop()  # 복구 : 부분해에서 삭제
            bUsed[i] = False  # 복구: 사용하지 않은 원소 

# 3번을 해보세요!
data = [n for n in input().split()]


# 출력합니다!
all_permutations(data)