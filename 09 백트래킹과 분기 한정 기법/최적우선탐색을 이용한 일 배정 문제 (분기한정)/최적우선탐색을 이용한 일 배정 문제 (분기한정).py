import heapq


# 일 배정 문제 (분기한정)
def job_assign_BFBnB(mat):
    N = len(mat)  # 사람과 일의 수
    Q = []  # 우선순위 큐 (최소힙 사용 )
    bound = calcBound(mat, [])  # 루트의 한계값 계산 
    heapq.heappush(Q, (bound+0,(0,bound,[])))

    while len(Q) >0:  # 큐가 공백이 아닌 동안 
        total, (cost, bound, jobs) = heapq.heappop(Q)  # 최소 노드 
        print("현재 노드: ", total, jobs)  # 탐색 중인 노드 출력 

        level = len(jobs)  # 배정된 일의 수 
        if level == N:  # 모두 배정되었으면 종료 
            return(total, jobs)

        for j in range(N):  # 모든 가능한 일에 대해 
            if j not in jobs:  # 아직 배정되지 않은 일 j에 대해
                jbs = jobs +[j]  # 배정된 일 추가
                cst = cost + mat[level][j]  # 새로운 확정 비용 
                bnd = calcBound(mat, jbs)  # 한계값(기대하한 )
                heapq.heappush(Q, (cst+bnd, (cst, bnd, jbs)))

# 일 배정 문제를 위한 서브 트리의 하한값 계산 
def calcBound(mat, jobs):
    N = len(mat)  # 전체 일의 수
    J = len(jobs)  # 이미 배정된 일의 개수
    bound = 0
    for i in range(J,N):  # 남은 각 사원에 대해 
        min = 9999
        for j in range(N):  # 모든 일에 대해
            if j not in jobs:  # 이미 배정된 일이 아니면 
                if min > mat[i][j]:
                    min = mat[i][j]
        bound += min
    return bound


# 3번을 해보세요!
n = int(input())

input_string = ""
for _ in range(n):
    line = input()
    input_string += line + "\n"
    
lines = input_string.strip().split("\n")
Man2Job = []
for line in lines:
    values = line.split()  # 공백을 기준으로 각 값을 분리
    Man2Job.append(list(map(int, values)))


# 출력합니다!
total, jobs = job_assign_BFBnB(Man2Job)
print("배정 결과: ", jobs)
print("전체 비용: ", total)